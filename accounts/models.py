from django.db import models
from django.contrib.auth.models import User
from shared.validators import validate_numeric

# Create your models here.
class Company(models.Model):
    CATEGORY_CHOICE = [
        
    ]
    name = models.CharField(max_length=100, verbose_name='نام شرکت')
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICE, verbose_name='دسته بندی کسب و کار')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=11, validators=[validate_numeric], verbose_name='شماره تلفن')
    created = models.DateTimeField(auto_now_add=True, verbose_name='زمان ثبت اطلاعات')
    updated = models.DateTimeField(auto_now=True, verbose_name='زمان آخرین بروزرسانی اطلاعات')
    
    class Meta:
        verbose_name = 'شرکت'
        verbose_name_plural = 'شرکت‌ها'
    
    
    def __str__(self):
        return self.name
    
    def get_user_username(self):
        return self.user.username
    get_user_username.short_description = 'نام کاربری'
    
    def get_user_email(self):
        return self.user.email
    get_user_username.short_description = 'ایمیل'
