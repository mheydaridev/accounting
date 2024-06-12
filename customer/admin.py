from django.contrib import admin
from .models import Customer, PhoneNumber

# Register your models here.
class PhoneNumberInline(admin.StackedInline):
    model = PhoneNumber
    extra = 1
    

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'get_jalali_birth_date', 'get_phone_numbers')
    list_filter = ('birth_date', 'updated', 'created')
    search_fields = ('name', 'location', 'get_jalali_birth_date')
    inlines = [PhoneNumberInline]
    ordering = ('-updated', '-created', '-birth_date')
    
    def get_phone_numbers(self, obj):
        return ", ".join([str(phone.phone_number) for phone in obj.phonenumber_set.all()])
    get_phone_numbers.short_description = 'شماره تلفن‌ها'


admin.site.register(Customer, CustomerAdmin)