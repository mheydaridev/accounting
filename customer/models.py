from django.db import models
from django.utils import timezone
from shared.validators import validate_numeric
from shared.utils import jalali_converter_date_time, jalali_converter_date

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام مشتری")
    location = models.TextField(blank=True, null=True, verbose_name="آدرس")
    birth_date = models.DateField(default=timezone.now, blank=True, null=True, verbose_name="تاریخ تولد")
    created = models.DateTimeField(auto_now_add=True, verbose_name='زمان ثبت اطلاعات')
    updated = models.DateTimeField(auto_now=True, verbose_name='زمان آخرین بروزرسانی اطلاعات')
    
    class Meta:
        verbose_name = "مشتری"
        verbose_name_plural = "مشتری‌ها"

    def __str__(self):
        return self.name
    
    def get_jalali_birth_date(self):
        return jalali_converter_date(self.birth_date)
    get_jalali_birth_date.short_description = 'تاریخ تولد'
    
    def get_jalali_created(self):
        return jalali_converter_date_time(self.created)
    get_jalali_created.short_description = 'زمان ثبت اطلاعات'

    def get_jalali_updated(self):
        return jalali_converter_date_time(self.updated)
    get_jalali_updated.short_description = 'زمان آخرین بروزرسانی اطلاعات'

    
class PhoneNumber(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='مشتری')
    phone_number = models.CharField(max_length=11, unique=True, blank=True, null=True, validators=[validate_numeric], verbose_name='شماره تلفن')
    
    class Meta:
        verbose_name = 'شماره تلفن'
        verbose_name_plural = 'شماره تلفن‌ها'

    def __str__(self):
        return str(self.phone_number)