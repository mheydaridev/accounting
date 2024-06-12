from django.db import models
from shared.utils import jalali_converter
from shared.validators import validate_numeric

# Create your models here.
class Supplier(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="نام تامین کننده")
    location = models.TextField(unique=True, blank=True, null=True, verbose_name="آدرس")
    website = models.URLField(unique=True, blank=True, null=True, verbose_name="وبسایت")
    created = models.DateTimeField(auto_now_add=True, verbose_name='زمان ثبت اطلاعات')
    updated = models.DateTimeField(auto_now=True, verbose_name='زمان آخرین بروزرسانی اطلاعات')

    class Meta:
        verbose_name = "تامین کننده"
        verbose_name_plural = "تامین کننده‌ها"

    def __str__(self):
        return self.name
    
    def get_jalali_created(self):
        return jalali_converter(self.created)
    get_jalali_created.short_description = 'زمان ثبت اطلاعات'

    def get_jalali_updated(self):
        return jalali_converter(self.updated)
    get_jalali_updated.short_description = 'زمان آخرین بروزرسانی اطلاعات'
    

class PhoneNumber(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name='انبار')
    phone_number = models.CharField(max_length=11, unique=True, blank=True, null=True, validators=[validate_numeric], verbose_name='شماره تلفن')
    
    class Meta:
        verbose_name = 'شماره تلفن'
        verbose_name_plural = 'شماره تلفن‌ها'

    def __str__(self):
        return str(self.phone_number)