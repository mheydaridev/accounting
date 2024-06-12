from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Inventory
from django.contrib import messages
from .forms import ProductAddForm, ProductUpdateForm, InventoryFormSet

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'product/product_list.html', context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    inventory = Inventory.objects.filter(product=product)
    context = {
        'product': product,
        'inventory': inventory,   
    }
    return render(request, 'product/product_detail.html', context)


def add_product(request):
    if request.method == 'POST':
        product_add_form = ProductAddForm(request.POST)
        if product_add_form.is_valid():
            product_add_form.save()
            messages.success(request, 'محصول جدید با موفقیت اصافه شد.', 'success')
            return redirect('product:product_list')
        else:
            context = {
                'product_add_form': product_add_form,
            }
    else:
        product_add_form = ProductAddForm()
        context = {
            'product_add_form': product_add_form,
        }
    return render(request, 'product/add_product.html', context)


def update_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product_update_form = ProductUpdateForm(request.POST, instance=product)
        inventory_form = InventoryFormSet(request.POST, instance=product)
        if product_update_form.is_valid() and inventory_form.is_valid():
            product_update_form.save()
            inventory_form.save()
            messages.success(request, 'اطلاعات محصول با موفقیت بروزرسانی شد.', 'success')
            return redirect('product:product_detail', product_id)
    else:
        product_update_form = ProductUpdateForm(instance=product)
        inventory_form = InventoryFormSet(instance=product)
        context = {
            'product': product,
            'product_update_form': product_update_form,
            'inventory_form': inventory_form,
        }          
    return render(request, 'product/update_product.html', context)


def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    context = {
        'product': product,
    }
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'محصول با موفقیت حذف شد.', 'success')
        return redirect('product:product_list')
    return render(request, 'product/confirm_delete_product.html', context)