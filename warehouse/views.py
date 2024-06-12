from django.shortcuts import render, get_object_or_404, redirect
from .models import Warehouse, PhoneNumber
from django.contrib import messages
from .forms import WarehouseAddForm, WarehouseUpdateForm, PhoneNumberFormSet

# Create your views here.
def warehouse_list(request):
    warehouses = Warehouse.objects.all()
    context = {
        'warehouses': warehouses,
    }
    return render(request, 'warehouse/warehouse_list.html', context)


def warehouse_detail(request, warehouse_id):
    warehouse = get_object_or_404(Warehouse, id=warehouse_id)
    phone_numbers = PhoneNumber.objects.filter(warehouse=warehouse)
    context = {
        'warehouse': warehouse,
        'phone_numbers': phone_numbers,
    }
    return render(request, 'warehouse/warehouse_detail.html', context)


def add_warehouse(request):
    if request.method == 'POST':
        warehouse_add_form = WarehouseAddForm(request.POST)
        if warehouse_add_form.is_valid():
            warehouse_add_form.save()
            messages.success(request, 'انبار جدید با موفقیت اصافه شد.', 'success')
            return redirect('warehouse:warehouse_list')
    else:
        warehouse_add_form = WarehouseAddForm()
        context = {
            'warehouse_add_form': warehouse_add_form,
        }
    return render(request, 'warehouse/add_warehouse.html', context)


def update_warehouse(request, warehouse_id):
    warehouse = get_object_or_404(Warehouse, id=warehouse_id)
    if request.method == 'POST':
        warehouse_update_form = WarehouseUpdateForm(request.POST, instance=warehouse)
        phone_numbers_form = PhoneNumberFormSet(request.POST, instance=warehouse)
        if warehouse_update_form.is_valid() and phone_numbers_form.is_valid():
            warehouse_update_form.save()
            phone_numbers_form.save()
            messages.success(request, 'اطلاعات انبار با موفقیت بروزرسانی شد.', 'success')
            return redirect('warehouse:warehouse_detail', warehouse_id)
    else:
        warehouse_update_form = WarehouseUpdateForm(instance=warehouse)
        phone_numbers_form = PhoneNumberFormSet(instance=warehouse)
        context = {
            'warehouse': warehouse,
            'warehouse_update_form': warehouse_update_form,
            'phone_numbers_form': phone_numbers_form,
        }          
    return render(request, 'warehouse/update_warehouse.html', context)


def delete_warehouse(request, warehouse_id):
    warehouse = get_object_or_404(Warehouse, id=warehouse_id)
    context ={
        'warehouse': warehouse,
    }
    if request.method == 'POST':
        warehouse.delete()
        messages.success(request, 'انبار با موفقیت حذف شد.', 'success')
        return redirect('warehouse:warehouse_list')
    return render(request, 'warehouse/confirm_delete_warehouse.html', context)