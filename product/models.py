from django.db import models
from warehouse.models import Warehouse
from shared.utils import jalali_converter

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='نام محصول')
    price = models.DecimalField(max_digits=12, decimal_places=0, default=0, verbose_name='قیمت')
    warehouse = models.ManyToManyField(Warehouse, through='Inventory')
    created = models.DateTimeField(auto_now_add=True, verbose_name='زمان ثبت اطلاعات')
    updated = models.DateTimeField(auto_now=True, verbose_name='زمان آخرین بروزرسانی اطلاعات')
    
    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def __str__(self):
        return self.name
    
    def get_jalali_created(self):
        return jalali_converter(self.created)
    get_jalali_created.short_description = 'زمان ثبت اطلاعات'

    def get_jalali_updated(self):
        return jalali_converter(self.updated)
    get_jalali_updated.short_description = 'زمان آخرین بروزرسانی اطلاعات'


class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, verbose_name='انبار')
    quantity = models.PositiveIntegerField(default=1, verbose_name='تعداد')

    class Meta:
        unique_together = ('product', 'warehouse')
        verbose_name = 'موجودی'
        verbose_name_plural = 'موجودی‌ها'

    def __str__(self):
        return f"{self.product.name} در {self.warehouse.branch}: {self.quantity}"