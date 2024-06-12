from django.contrib import admin
from .models import Warehouse, PhoneNumber

# Register your models here.
class PhoneNumberInline(admin.StackedInline):
    model = PhoneNumber
    extra = 1


class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('branch', 'location', 'get_phone_numbers')
    list_filter = ('updated', 'created')
    search_fields = ('branch', 'location')
    inlines = (PhoneNumberInline,)
    ordering = ('-updated', '-created')

    def get_phone_numbers(self, obj):
        return ", ".join([str(phone.phone_number) for phone in obj.phonenumber_set.all()])
    get_phone_numbers.short_description = 'شماره تلفن‌ها'


admin.site.register(Warehouse, WarehouseAdmin)