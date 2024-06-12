from django.contrib import admin
from .models import SalesInvoice, InvoiceItem

# Register your models here.
class InvoiceItemInline(admin.StackedInline):
    model = InvoiceItem
    extra = 1

class SalesInvoiceAdmin(admin.ModelAdmin):
    list_display = ('get_customer_name', 'get_warehouse_branch', 'invoice_total_price', 'get_jalali_invoice_date')
    list_filter = ('updated', 'created', 'invoice_date', 'customer__name', 'warehouse__branch')
    search_fields = ('customer__name', 'warehouse__branch')
    inlines = [InvoiceItemInline,]
    ordering = ('-updated', '-created', '-invoice_date', 'customer__name', 'warehouse__branch')


admin.site.register(SalesInvoice, SalesInvoiceAdmin)