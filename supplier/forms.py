from django import forms
from .models import Supplier, PhoneNumber
from shared.validators import validate_numeric
from django.forms import inlineformset_factory


class SupplierAddForm(forms.ModelForm):
    phone_number = forms.CharField(max_length=11, required=False, label='شماره تلفن', validators=[validate_numeric])
    
    class Meta:
        model = Supplier
        fields = ('name', 'location', 'website')

    def save(self):
        supplier = super().save()
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number:
            PhoneNumber.objects.create(supplier=supplier, phone_number=phone_number)
        return supplier
    
    
class SupplierUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Supplier
        fields = ('name', 'location', 'website')


class PhoneNumberUpdateForm(forms.ModelForm):
    
    class Meta:
        model = PhoneNumber
        fields = ('phone_number',)
        
        
PhoneNumberFormSet = inlineformset_factory(Supplier, PhoneNumber, form=PhoneNumberUpdateForm, extra=1, can_delete=True)