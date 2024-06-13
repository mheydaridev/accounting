from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Company

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'نام کاربری'
        self.fields['password1'].label = 'رمز عبور'
        self.fields['password2'].label = 'تکرار رمز عبور'


class CompanyRegisterForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = Company
        fields = ['name', 'category', 'phone_number', 'email']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = 'نام شرکت'
        self.fields['category'].label = 'دسته بندی کسب و کار'
        self.fields['phone_number'].label = 'شماره تلفن'
        self.fields['email'].label = 'ایمیل'


class CompanyUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Company
        fields = ['name', 'category', 'email', 'phone_number']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = 'نام شرکت'
        self.fields['category'].label = 'دسته بندی کسب و کار'
        self.fields['email'].label = 'ایمیل'
        self.fields['phone_number'].label = 'شماره تلفن'