from django.urls import path
from .views import purchase_invoice_list, purchase_invoice_detail, add_purchase_invoice, update_purchase_invoice, delete_purchase_invoice

app_name = 'purchase_invoice'
urlpatterns = [
    path('', purchase_invoice_list, name='purchase_invoice_list'),
    path('detail/<int:purchase_invoice_id>/', purchase_invoice_detail, name='purchase_invoice_detail'),
    path('add/', add_purchase_invoice, name='add_purchase_invoice'),
    path('update/<int:purchase_invoice_id>/', update_purchase_invoice, name='update_purchase_invoice'),
    path('delete/<int:purchase_invoice_id>/', delete_purchase_invoice, name='delete_purchase_invoice'),
]