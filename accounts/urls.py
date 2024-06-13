from django.urls import path
from .views import company_register, company_register_information, login, profile, update_company, change_password, logout, delete_account

app_name = 'accounts'
urlpatterns = [
    path('register/company/', company_register, name='company_register'),
    path('register/company_information/', company_register_information, name='company_register_information'),
    path('login/', login, name='login'),
    path('profile/<int:company_id>/', profile, name='company_detail'),
    path('update_company/<int:company_id>/', update_company, name='update_company'),
    path('password/change/', change_password, name='change_password'),
    path('logout/<int:company_id>/', logout, name='logout'),
    path('delete_account/<int:company_id>/', delete_account, name='delete_account')
]