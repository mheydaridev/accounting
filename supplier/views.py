from django.shortcuts import render, get_object_or_404, redirect
from .models import Supplier, PhoneNumber
from django.contrib import messages
from .forms import SupplierAddForm, SupplierUpdateForm, PhoneNumberFormSet

# Create your views here.
def supplier_list(request):
    suppliers = Supplier.objects.all()
    context = {
        'suppliers': suppliers,
    }
    return render(request, 'supplier/supplier_list.html', context)


def supplier_detail(request, supplier_id):
    supplier = get_object_or_404(Supplier, id=supplier_id)
    phone_numbers = PhoneNumber.objects.filter(supplier=supplier)
    context = {
        'supplier': supplier,
        'phone_numbers': phone_numbers,
    }
    return render(request, 'supplier/supplier_detail.html', context)


def add_supplier(request):
    if request.method == 'POST':
        supplier_add_form = SupplierAddForm(request.POST)
        if supplier_add_form.is_valid():
            supplier_add_form.save()
            messages.success(request, 'تأمین کننده جدید با موفقیت اصافه شد.', 'success')
            return redirect('supplier:supplier_list')
    else:
        supplier_add_form = SupplierAddForm()
        context = {
            'supplier_add_form': supplier_add_form,
        }
    return render(request, 'supplier/add_supplier.html', context)


def update_supplier(request, supplier_id):
    supplier = get_object_or_404(Supplier, id=supplier_id)
    if request.method == 'POST':
        supplier_update_form = SupplierUpdateForm(request.POST, instance=supplier)
        phone_numbers_form = PhoneNumberFormSet(request.POST, instance=supplier)
        if supplier_update_form.is_valid() and phone_numbers_form.is_valid():
            supplier_update_form.save()
            phone_numbers_form.save()
            messages.success(request, 'اطلاعات تأمین کننده با موفقیت بروزرسانی شد.', 'success')
            return redirect('supplier:supplier_detail', supplier_id)
    else:
        supplier_update_form = SupplierUpdateForm(instance=supplier)
        phone_numbers_form = PhoneNumberFormSet(instance=supplier)
        context = {
            'supplier': supplier,
            'supplier_update_form': supplier_update_form,
            'phone_numbers_form': phone_numbers_form,
        }          
    return render(request, 'supplier/update_supplier.html', context)


def delete_supplier(request, supplier_id):
    supplier = get_object_or_404(Supplier, id=supplier_id)
    context = {
        'supplier': supplier
    }
    if request.method == 'POST':
        supplier.delete()
        messages.success(request, 'تأمین کننده با موفقیت حذف شد.', 'success')
        return redirect('supplier:supplier_list')
    return render(request, 'supplier/confirm_delete_supplier.html', context)