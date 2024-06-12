from django import forms
from .models import Product, Inventory
from warehouse.models import Warehouse
from django.forms import inlineformset_factory


class ProductAddForm(forms.ModelForm):
    quantity = forms.IntegerField(label='تعداد')
    warehouse = forms.ModelChoiceField(queryset=Warehouse.objects.all(), label='شعبه انبار')

    class Meta:
        model = Product
        fields = ('name', 'price')

    def save(self):
        product = super().save()
        warehouse = self.cleaned_data.get('warehouse')
        quantity = self.cleaned_data.get('quantity')
        if warehouse and quantity:
            Inventory.objects.create(product=product, warehouse=warehouse, quantity=quantity)
        return product
    

class ProductUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = ('name', 'price')
    

class InventoryUpdateForm(forms.ModelForm):
     
    class Meta:
        model = Inventory
        fields = ('quantity', 'warehouse')
        

InventoryFormSet = inlineformset_factory(Product, Inventory, form=InventoryUpdateForm, extra=1, can_delete=True)