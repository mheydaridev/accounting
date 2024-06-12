from django.shortcuts import render, get_object_or_404, redirect
from .models import Customer, PhoneNumber
from django.contrib import messages
from .forms import CustomerAddForm, CustomerUpdateForm, PhoneNumberFormSet

# Create your views here.
def customer_list(request):
    customers = Customer.objects.all()
    context = {
        'customers': customers,
    }
    return render(request, 'customer/customer_list.html', context)


def customer_detail(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    phone_numbers = PhoneNumber.objects.filter(customer=customer)
    context = {
        'customer': customer,
        'phone_numbers': phone_numbers,   
    }
    return render(request, 'customer/customer_detail.html', context)


def add_customer(request):
    if request.method == 'POST':
        customer_add_form = CustomerAddForm(request.POST)
        if customer_add_form.is_valid():
            customer_add_form.save()
            messages.success(request, 'انبار جدید با موفقیت اصافه شد.', 'success')
            return redirect('customer:customer_list')
    else:
        customer_add_form = CustomerAddForm()
        context = {
            'customer_add_form': customer_add_form
        }
    return render(request, 'customer/add_customer.html', context)


def update_customer(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    if request.method == 'POST':
        customer_update_form = CustomerUpdateForm(request.POST, instance=customer)
        phone_numbers_form = PhoneNumberFormSet(request.POST, isinstance=customer)
        if customer_update_form.is_valid() and phone_numbers_form.is_valid():
            customer_update_form.save()
            phone_numbers_form.save()
            messages.success(request, 'اطلاعات انبار با موفقیت بروزرسانی شد.', 'success')
            return redirect('customer:customer_detail', customer_id)
    else:
        customer_update_form = CustomerUpdateForm(instance=customer)
        phone_numbers_form = PhoneNumberFormSet(instance=customer)
        context = {
            'customer': customer,
            'customer_update_form': customer_update_form,
            'phone_numbers_form': phone_numbers_form,
        }          
    return render(request, 'customer/update_customer.html', context)


def delete_customer(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    context = {
        'customer': customer,
    }
    if request.method == 'POST':
        customer.delete()
        messages.success(request, 'انبار با موفقیت حذف شد.', 'success')
        return redirect('customer:customer_list')
    return render(request, 'customer/confirm_delete_customer.html', context)