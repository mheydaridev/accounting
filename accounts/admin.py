from django.contrib import admin
from .models import Company


class ComponyAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'get_user_username', 'get_user_email', 'phone_number')
    list_filter = ('category', 'updated', 'created')
    search_fields = ('name', 'user__username', 'phone_number')
    ordering = ('-updated', '-created', 'name')
    

admin.site.register(Company, ComponyAdmin)