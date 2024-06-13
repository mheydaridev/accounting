from django.db import models
from warehouse.models import Warehouse
from supplier.models import Supplier
from product.models import Product, Inventory
from shared.utils import jalali_converter_date_time, jalali_converter_date
from decimal import Decimal

# Create your models here.
class PurchaseInvoice(models.Model):
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, verbose_name='انبار')
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name='تأمین کننده')
    invoice_date = models.DateField(verbose_name='تاریخ فاکتور')
    value_added = models.PositiveIntegerField(blank=True, null=True,verbose_name='درصد ارزش افزوده فاکتور')
    created = models.DateTimeField(auto_now_add=True, verbose_name='زمان ثبت اطلاعات')
    updated = models.DateTimeField(auto_now=True, verbose_name='زمان آخرین بروزرسانی اطلاعات')
    
    class Meta:
        verbose_name = 'فاکتور خرید'
        verbose_name_plural = 'فاکتورهای خرید'
        
    def __str__(self):
        return str(self.get_jalali_invoice_date)
    
    def invoice_total_price(self):
        invoice_items = InvoiceItem.objects.filter(purchase_invoice=self.id)
        invoice_total_price = 0
        for invoice_item in invoice_items:
            invoice_total_price += invoice_item.product_total_price()
        return invoice_total_price
    invoice_total_price.short_decription = 'قیمت کل فاکتور'
    
    def get_jalali_invoice_date(self):
        return jalali_converter_date(self.invoice_date)
    get_jalali_invoice_date.short_description = 'تاریخ فاکتور'

    def get_jalali_created(self):
        return jalali_converter_date_time(self.created)
    get_jalali_created.short_description = 'زمان ثبت اطلاعات'

    def get_jalali_updated(self):
        return jalali_converter_date_time(self.updated)
    get_jalali_updated.short_description = 'زمان آخرین بروزرسانی اطلاعات'
    
    def get_supplier_name(self):
        return self.supplier.name
    get_supplier_name.short_description = 'نام تأمین کننده'
    
    def get_warehouse_branch(self):
        return self.warehouse.branch
    get_warehouse_branch.short_description = 'شعبه انبار'
    

class InvoiceItem(models.Model):
    purchase_invoice = models.ForeignKey(PurchaseInvoice, on_delete=models.CASCADE, verbose_name='فاکتور خرید')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='purchase_invoice_items', verbose_name='محصول')
    quantity = models.PositiveIntegerField(default=1, verbose_name='تعداد')
    unit_price = models.DecimalField(max_digits=12, decimal_places=0, verbose_name='قیمت محصول')
    value_added = models.PositiveIntegerField(blank=True, null=True,verbose_name='درصد ارزش افزوده محصول')

    class Meta:
        verbose_name = 'آیتم فاکتور'
        verbose_name_plural = 'آیتم‌های فاکتور'
    
    def product_total_price(self):
        return self.quantity * self.unit_price
    product_total_price.short_decription = 'جمع قیمت محصول'
    
    def get_product_name(self):
        return self.product.name
    get_product_name.short_description = 'نام محصول'
    
    def save(self, *args, **kwargs):    
        # Upadate product price
        unit_price = self.unit_price
        total_value_added = self.purchase_invoice.value_added
        unit_value_added = self.value_added
        if total_value_added and unit_value_added:
            self.product.price = unit_price * (total_value_added / Decimal(100)) * (unit_value_added / Decimal(100))
        elif total_value_added:
            self.product.price = unit_price * (total_value_added / Decimal(100))
        elif unit_value_added:
            self.product.price = unit_price * (unit_value_added / Decimal(100))
        else:
            self.product.price = unit_price
        # Increase inventory
        inventory = Inventory.objects.get(product=self.product, warehouse=self.purchase_invoice.warehouse)
        inventory.quantity += self.quantity
        inventory.save()
        super().save(*args, **kwargs)