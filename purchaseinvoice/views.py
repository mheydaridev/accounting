from django.shortcuts import render, get_object_or_404
from .models import PurchaseInvoice, InvoiceItem

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
    pass


def update_purchase_invoice(request):
    pass


def delete_purchase_invoice(request):
    pass
