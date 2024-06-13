from django.shortcuts import render, get_object_or_404, redirect
from .models import SalesInvoice, InvoiceItem
from .forms import SalesInvoiceForm, InvoiceItemForm
from django.contrib import messages

# Create your views here.
def sales_invoice_list(request):
    sales_invoices = SalesInvoice.objects.all()
    context = {
        'sales_invoices': sales_invoices,
    }
    return render(request, 'salesinvoice/sales_invoice_list.html', context)


def sales_invoice_detail(request, sales_invoice_id):
    sales_invoice = get_object_or_404(SalesInvoice, sales_invoice_id)
    invoice_items = InvoiceItem.objects.filter(sales_invoice=sales_invoice)
    context = {
        'sales_invoice': sales_invoice,
        'invoice_items': invoice_items,
    }
    return render(request, 'salesinvoice/sales_invoice_detail.html', context)


def add_sales_invoice(request):
    if request.method == 'POST':
        sales_invoice_form = SalesInvoiceForm(request.POST)
        if sales_invoice_form.is_valid():
            sales_invoice = sales_invoice_form.save()
            for product_data in request.POST.getlist('products'):
                product_id = product_data.get('product')
                quantity = product_data.get('quantity')
                unit_price = product_data.get('unit_price')
                discount = product_data.get('discount')
                InvoiceItem.objects.create(
                    sales_invoice=sales_invoice,
                    product_id=product_id,
                    quantity=quantity,
                    unit_price=unit_price,
                    discount=discount,
                )
            messages.success(request, 'فاکتور جدید با موفقیت ایجاد شد.', 'success')
            return redirect('sales_invoice:sales_invoice_list')
    else:
        sales_invoice_form = SalesInvoiceForm()
        invoice_item_form = InvoiceItemForm()
        context = {
            'sales_invoice_form': sales_invoice_form,
            'invoice_item_form': invoice_item_form,
        }
    return render(request, 'salesinvoice/add_sales_invoice.html', context)


def update_sales_invoice(request, sales_invoice_id):
    sales_invoice = get_object_or_404(SalesInvoice, id=sales_invoice_id)
    invoice_items = InvoiceItem.objects.filter(sales_invoice=sales_invoice)    
    if request.method == 'POST':
        sales_invoice_form = SalesInvoiceForm(request.POST, instance=sales_invoice)
        if sales_invoice_form.is_valid():
            sales_invoice_form.save()
            for item_id, product_id, quantity, unit_price, value_added in zip(
                request.POST.getlist('item_id'),
                request.POST.getlist('product'),
                request.POST.getlist('quantity'),
                request.POST.getlist('unit_price'),
                request.POST.getlist('value_added')
            ):
                if item_id:
                    invoice_item = InvoiceItem.objects.get(id=item_id)
                    invoice_item.product = product_id
                    invoice_item.quantity = quantity
                    invoice_item.unit_price = unit_price
                    invoice_item.value_added = value_added
                    invoice_item.save()
                else:
                    InvoiceItem.objects.create(
                        sales_invoice=sales_invoice,
                        product_id=product_id,
                        quantity=quantity,
                        unit_price=unit_price,
                        value_added=value_added
                    )
            messages.success(request, 'فاکتور با موفقیت بروزرسانی شد.', 'success')
            return redirect('sales_invoice:sales_invoice_detail', sales_invoice_id)
    else:
        sales_invoice_form = SalesInvoiceForm(instance=sales_invoice)
        item_forms = [InvoiceItemForm(instance=item) for item in invoice_items]
        context = {
            'sales_invoice_form': sales_invoice_form,
            'item_forms': item_forms,
            'sales_invoice_id': sales_invoice_id,
        }
    return render(request, 'salesinvoice/update_sales_invoice.html', context)


def delete_sales_invoice(request, sales_invoice_id):
    sales_invoice = get_object_or_404(SalesInvoice, id=sales_invoice_id)
    context = {
        'sales_invoice': sales_invoice,
    }
    if request.method == 'POST':
        sales_invoice.delete()
        messages.success(request, 'فاکتور با موفقیت حذف شد.', 'success')
        return redirect('sales_invoice:sales_invoice_list')
    return render(request, 'salesinvoice/confirm_delete_sales_invoice.html', context)