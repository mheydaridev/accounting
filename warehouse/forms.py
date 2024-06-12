from django import forms
from .models import Warehouse, PhoneNumber
from shared.validators import validate_numeric
from django.forms import inlineformset_factory


class WarehouseAddForm(forms.ModelForm):
    phone_number = forms.CharField(max_length=11, required=False, validators=[validate_numeric], label='شماره تلفن')
    
    class Meta:
        model = Warehouse
        fields = ('branch', 'location')

    def save(self):
        warehouse = super().save()
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number:
            PhoneNumber.objects.create(warehouse=warehouse, phone_number=phone_number)
        return warehouse


class WarehouseUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Warehouse
        fields = ('branch', 'location')


class PhoneNumberUpdateForm(forms.ModelForm):
    
    class Meta:
        model = PhoneNumber
        fields = ('phone_number',)
        
        
PhoneNumberFormSet = inlineformset_factory(Warehouse, PhoneNumber, form=PhoneNumberUpdateForm, extra=1, can_delete=True)