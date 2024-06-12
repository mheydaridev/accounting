from django.urls import path
from .views import customer_list, customer_detail, add_customer, update_customer, delete_customer

app_name = 'customer'
urlpatterns = [
    path('', customer_list, name='customer_list'),
    path('detail/<int:customer_id>/', customer_detail, name='customer_detail'),
    path('add/', add_customer, name='add_customer'),
    path('update/<int:customer_id>/', update_customer, name='update_customer'),
    path('delete/<int:customer_id>/', delete_customer, name='delete_customer'),
]