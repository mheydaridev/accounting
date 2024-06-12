from django.urls import path
from .views import sales_invoice_list, sales_invoice_detail, add_sales_invoice, update_sales_invoice, delete_sales_invoice

app_name = 'sales_invoice'
urlpatterns = [
    path('', sales_invoice_list, name='sales_invoice_list'),
    path('detail/<int:sales_invoice_id>/', sales_invoice_detail, name='sales_invoice_detail'),
    path('add/', add_sales_invoice, name='add_sales_invoice'),
    path('update/<int:sales_invoice_id>/', update_sales_invoice, name='update_sales_invoice'),
    path('delete/<int:sales_invoice_id>/', delete_sales_invoice, name='delete_sales_invoice'),
]