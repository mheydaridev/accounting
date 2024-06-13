from django.shortcuts import render, get_object_or_404, redirect
from .models import PurchaseInvoice, InvoiceItem
from .forms import PurchaseInvoiceForm, InvoiceItemForm
from django.contrib import messages

# Create your views here.
def purchase_invoice_list(request):
    purchase_invoices = PurchaseInvoice.objects.all()
    context = {
        'purchase_invoices': purchase_invoices,
    }
    return render(request, 'purchaseinvoice/purechare_invoice_list.html', context)


def purchase_invoice_detail(request, purchase_invoice_id):
    purchase_invoice = get_object_or_404(PurchaseInvoice, purchase_invoice_id)
    invoice_items = InvoiceItem.objects.filter(purchase_invoice=purchase_invoice)
    context = {
        'purchase_invoice': purchase_invoice,
        'invoice_items': invoice_items,
    }
    return render(request, 'purchaseinvoice/purchase_invoice_detail.html', context)


def add_purchase_invoice(request):
    if request.method == 'POST':
        purchase_invoice_form = PurchaseInvoiceForm(request.POST)
        if purchase_invoice_form.is_valid():
            purchase_invoice = purchase_invoice_form.save()
            for product_data in request.POST.getlist('products'):
                product_id = product_data.get('product')
                quantity = product_data.get('quantity')
                unit_price = product_data.get('unit_price')
                value_added = product_data.get('value_added')
                InvoiceItem.objects.create(
                    purchase_invoice=purchase_invoice,
                    product_id=product_id,
                    quantity=quantity,
                    unit_price=unit_price,
                    value_added=value_added,
                )
            messages.success(request, 'فاکتور جدید با موفقیت ایجاد شد.', 'success')
            return redirect('purchase_invoice:purchase_invoice_list')
    else:
        purchase_invoice_form = PurchaseInvoiceForm()
        invoice_item_form = InvoiceItemForm()
        context = {
            'purchase_invoice_form': purchase_invoice_form,
            'invoice_item_form': invoice_item_form,
        }
    return render(request, 'purchaseinvoice/add_purchase_invoice.html', context)


def update_purchase_invoice(request, purchase_invoice_id):
    purchase_invoice = get_object_or_404(PurchaseInvoice, id=purchase_invoice_id)
    invoice_items = InvoiceItem.objects.filter(purchase_invoice=purchase_invoice)    
    if request.method == 'POST':
        purchase_invoice_form = PurchaseInvoiceForm(request.POST, instance=purchase_invoice)
        if purchase_invoice_form.is_valid():
            purchase_invoice_form.save()
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
                        purchase_invoice=purchase_invoice,
                        product_id=product_id,
                        quantity=quantity,
                        unit_price=unit_price,
                        value_added=value_added
                    )
            return redirect('purchase_invoice:purchase_invoice_detail', purchase_invoice_id)
    else:
        purchase_invoice_form = PurchaseInvoiceForm(instance=purchase_invoice)
        item_forms = [InvoiceItemForm(instance=item) for item in invoice_items]
        context = {
            'purchase_invoice_form': purchase_invoice_form,
            'item_forms': item_forms,
            'purchase_invoice_id': purchase_invoice_id,
        }
    return render(request, 'purchaseinvoice/update_purchase_invoice.html', context)


def delete_purchase_invoice(request, purchase_invoice_id):
    purchase_invoice = get_object_or_404(PurchaseInvoice, id=purchase_invoice_id)
    context = {
        'purchase_invoice': purchase_invoice,
    }
    if request.method == 'POST':
        purchase_invoice.delete()
        messages.success(request, 'فاکتور با موفقیت حذف شد.', 'success')
        return redirect('purchase_invoice:purchase_invoice_list')
    return render(request, 'purchaseinvoice/delete_purchase_invoice.html', context)



