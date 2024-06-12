from django import forms
from .models import Customer, PhoneNumber
from shared.validators import validate_numeric
from django.forms import inlineformset_factory


class CustomerAddForm(forms.ModelForm):
    phone_number = forms.CharField(max_length=11, required=False, validators=[validate_numeric], label='شماره تلفن')
    
    class Meta:
        model = Customer
        fields = ('name', 'location', 'birth_date')

    def save(self):
        customer = super().save()
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number:
            PhoneNumber.objects.create(customer=customer, phone_number=phone_number)
        return customer
    
    
class CustomerUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Customer
        fields = ('name', 'location', 'birth_date')
    

class PhoneNumberUpdateForm(forms.ModelForm):
    
    class Meta:
        model = PhoneNumber
        fields = ('phone_number',)

    
PhoneNumberFormSet = inlineformset_factory(Customer, PhoneNumber, form=PhoneNumberUpdateForm, extra=1, can_delete=True)