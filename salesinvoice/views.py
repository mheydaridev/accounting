from django.shortcuts import render, get_object_or_404
from .models import SalesInvoice, InvoiceItem

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
    pass


def update_sales_invoice(request):
    pass


def delete_sales_invoice(request):
    pass