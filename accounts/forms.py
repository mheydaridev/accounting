# from django import forms
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from .models import CustomUser


# class CustomUserRegisterForm(UserCreationForm):
#     password = forms.CharField(
#         label='رمز',
#         widget=forms.PasswordInput(attrs={'class': 'form-control'}),
#     )
#     confirm_password = forms.CharField(
#         label='تائید رمز',
#         widget=forms.PasswordInput(attrs={'class': 'form-control'}),
#     )
    
#     class Meta(UserCreationForm.Meta):
#         model = CustomUser
#         fields = UserCreationForm.Meta.fields + ('phone_number',)
    
#     def clean_password2(self):
#         password = self.cleaned_data.get('password')
#         confirm_password = self.cleaned_data.get('confirm_password')

#         if password and confirm_password and password != confirm_password:
#             raise forms.ValidationError("رمز و تکرار آن با هم برابر نیستند.")

#         return password


# class CustomUserUpdateForm(UserChangeForm):
#     class Meta:
#         model = CustomUser
#         fields = UserChangeForm.Meta.fields


# class CustomUserLoginForm(forms.Form):
#     username = forms.CharField(max_length=254, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     password = forms.CharField(max_length=32, min_length=8, widget=forms.PasswordInput(attrs={'class': 'form-control'}))