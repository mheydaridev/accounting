from django.db import models
from warehouse.models import Warehouse
from customer.models import Customer
from product.models import Product, Inventory
from shared.utils import jalali_converter
from django.core.exceptions import ValidationError

# Create your models here.
class SalesInvoice(models.Model):
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, verbose_name='انبار')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='مشتری')
    invoice_date = models.DateField(verbose_name='تاریخ فاکتور')
    created = models.DateTimeField(auto_now_add=True, verbose_name='زمان ثبت اطلاعات')
    updated = models.DateTimeField(auto_now=True, verbose_name='زمان آخرین بروزرسانی اطلاعات')
    
    class Meta:
        verbose_name = 'فاکتور فروش'
        verbose_name_plural = 'فاکتورهای فروش'

    def __str__(self):
        return str(self.get_jalali_invoice_date)
    
    def invoice_total_price(self):
        invoice_item = InvoiceItem.objects.filter(sales_invoice=self.id)
        invoice_total_price = 0
        for product_total_price in invoice_item.product_total_price:
            invoice_total_price += product_total_price
        return invoice_total_price
    invoice_total_price.short_decription = 'قیمت کل فاکتور'
    
    def get_jalali_invoice_date(self):
        return jalali_converter(self.invoice_date)
    get_jalali_invoice_date.short_description = 'تاریخ فاکتور'
        
    def get_jalali_created(self):
        return jalali_converter(self.created)
    get_jalali_created.short_description = 'زمان ثبت اطلاعات'

    def get_jalali_updated(self):
        return jalali_converter(self.updated)
    get_jalali_updated.short_description = 'زمان آخرین بروزرسانی اطلاعات'
    
    def get_customer_name(self):
        return self.customer.name
    get_customer_name.short_description = 'نام مشتری'
    
    def get_warehouse_branch(self):
        return self.warehouse.branch
    get_warehouse_branch.short_description = 'شعبه انبار'

class InvoiceItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='sales_invoice_items', verbose_name='محصول')
    sales_invoice = models.ForeignKey(SalesInvoice, on_delete=models.CASCADE, verbose_name='فاکتور فروش')
    quantity = models.PositiveIntegerField(default=1, verbose_name='تعداد')
    unit_price = models.DecimalField(max_digits=12, decimal_places=0, verbose_name='قیمت محصول')
    discount = models.PositiveIntegerField(blank=True, null=True, verbose_name='درصد تخفیف')
    
    class Meta:
        verbose_name = 'آیتم فاکتور'
        verbose_name_plural = 'آیتم‌های فاکتور'
    
    def get_product_price(self):
        return self.product.price
    get_product_price.short_decription = 'قیمت محصول'
    
    def product_total_price(self):
        if self.discount:
            return self.quantity * self.unit_price * (1 - self.discount / 100)
        else:
            return self.quantity * self.unit_price
    product_total_price.short_decription = 'جمع قیمت محصول'
    
    def get_product_name(self):
        return self.product.name
    get_product_name.short_description = 'نام محصول'
    
    def save(self, *args, **kwargs):
        if not self.unit_price:
            self.unit_price = self.get_product_price()
        # Check inventory
        inventory = Inventory.objects.get(product=self.product, warehouse=self.sales_invoice.warehouse)
        if inventory.quantity < self.quantity:
            raise ValidationError(f"موجودی کافی برای محصول {self.product.name} در انبار {self.sales_invoice.warehouse.branch} وجود ندارد.")
        # Reduce inventory
        inventory.quantity -= self.quantity
        inventory.save()
        super().save(*args, **kwargs)