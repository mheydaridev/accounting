from django.urls import path
from .views import product_list, product_detail, add_product, update_product, delete_product

app_name = 'product'
urlpatterns = [
    path('', product_list, name='product_list'),
    path('detail/<int:product_id>/', product_detail, name='product_detail'),
    path('add/', add_product, name='add_product'),
    path('update/<int:product_id>/', update_product, name='update_product'),
    path('delete/<int:product_id>/', delete_product, name='delete_product'),
]