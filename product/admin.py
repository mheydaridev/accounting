from django.contrib import admin
from .models import Product, Inventory

# Register your models here.
class InventoryInline(admin.StackedInline):
    model = Inventory
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    list_filter = ('updated', 'created')
    search_fields = ('name', 'price')
    inlines = (InventoryInline,)
    ordering = ('-updated', '-created', '-price')


admin.site.register(Product, ProductAdmin)