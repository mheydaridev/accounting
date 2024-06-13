from django.contrib import admin
from .models import PurchaseInvoice, InvoiceItem

# Register your models here.
class InvoiceItemInline(admin.StackedInline):
    model = InvoiceItem
    extra = 1

class PurchaseInvoiceAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'get_supplier_name', 'get_warehouse_branch', 'invoice_total_price', 'get_jalali_invoice_date')
    list_filter = ('updated', 'created', 'invoice_date', 'supplier__name', 'warehouse__branch')
    search_fields = ('supplier__name', 'warehouse_branch')
    inlines = [InvoiceItemInline,]
    ordering = ('-updated', '-created', '-invoice_date', 'supplier__name', 'warehouse__branch')


admin.site.register(PurchaseInvoice, PurchaseInvoiceAdmin)