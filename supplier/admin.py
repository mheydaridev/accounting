from django.contrib import admin
from .models import Supplier, PhoneNumber

# Register your models here.
class PhoneNumberInline(admin.StackedInline):
    model = PhoneNumber
    extra = 1


class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'website', 'get_phone_numbers')
    list_filter = ('updated', 'created')
    search_fields = ('name', 'location')
    inlines = (PhoneNumberInline,)
    ordering = ('-updated', '-created')
    
    def get_phone_numbers(self, obj):
        return ", ".join([str(phone.phone_number) for phone in obj.phonenumber_set.all()])
    get_phone_numbers.short_description = 'شماره تلفن‌ها'


admin.site.register(Supplier, SupplierAdmin)