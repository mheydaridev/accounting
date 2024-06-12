from django.urls import path
from .views import supplier_list, supplier_detail, add_supplier, update_supplier, delete_supplier

app_name = 'supplier'
urlpatterns = [
    path('', supplier_list, name='supplier_list'),
    path('detail/<int:supplier_id>/', supplier_detail, name='supplier_detail'),
    path('add/', add_supplier, name='add_supplier'),
    path('update/<int:supplier_id>/', update_supplier, name='update_supplier'),
    path('delete/<int:supplier_id>/', delete_supplier, name='delete_supplier'),
]