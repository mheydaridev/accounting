from django.urls import path
from .views import warehouse_list, warehouse_detail, add_warehouse, update_warehouse, delete_warehouse

app_name = 'warehouse'
urlpatterns = [
    path('', warehouse_list, name='warehouse_list'),
    path('detail/<int:warehouse_id>/', warehouse_detail, name='warehouse_detail'),
    path('add/', add_warehouse, name='add_warehouse'),
    path('update/<int:warehouse_id>/', update_warehouse, name='update_warehouse'),
    path('delete/<int:warehouse_id>/', delete_warehouse, name='delete_warehouse'),
]