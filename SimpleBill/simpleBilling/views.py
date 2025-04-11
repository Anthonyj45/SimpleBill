from django.shortcuts import render, redirect
from .models import Client, Invoice, Attachment
from decimal import Decimal
from .forms import InvoiceForm
from django.http import JsonResponse

def create_invoice_view(request):
    if request.method == 'POST':
        client_name = request.POST.get('client_name')
        service_fee = Decimal(request.POST.get('service_fee'))
        travel_expenses = Decimal(request.POST.get('travel_expenses'))
        tax_percent = Decimal(request.POST.get('tax_percent'))
        uploaded_files = request.FILES.getlist('attachments')
        
        client, _ = Client.objects.get_or_create(name=client_name)
        
        invoice = Invoice.objects.create(
            client=client,
            service_fee=service_fee,
            travel_expenses=travel_expenses,
            tax_percent=tax_percent,
        )
        
        for file in uploaded_files:
            Attachment.objects.create(invoice=invoice, file=file)
            
        return redirect('invoice-success')
    
    return render(request, 'simpleBilling/invoice.html')
    
        
def invoice_success_view(request):
    return render(request, 'simpleBilling/success.html')

def invoice_list_create_view(request):
    invoices = Invoice.objects.select_related("client").prefetch_related("attachments").order_by("-billing_date")
    
    if request.method == "POST":
        client_name = request.POST.get("client_name")
        service_fee = Decimal(request.POST.get("service_fee"))
        travel_expenses = Decimal(request.POST.get("travel_expenses"))
        tax_percent = Decimal(request.POST.get("tax_percent"))
        uploaded_files = request.FILES.getlist("attachments")
        
        client, _ = Client.objects.get_or_create(name=client_name)
        
        invoice = Invoice.objects.create(
            client=client,
            service_fee=service_fee,
            travel_expenses=travel_expenses,
            tax_percent=tax_percent,
        )
        
        for file in uploaded_files:
            Attachment.objects.create(invoice=invoice, file=file)
            
        if request.headers.get("x-requested-with") == "XMLHttpRequest":
            return JsonResponse({
                'success': True,
                'invoice': {
                    'id': invoice.id,
                    'client': client_name,
                    'service_fee': str(invoice.service_fee),
                    'travel_expenses': str(invoice.travel_expenses),
                    'tax_percent': str(invoice.tax_percent),
                    'total': str(invoice.total),
                }
            })
        
        return redirect('invoice-success')
    
    return render(request, "simpleBilling/invoice.html", {
        'invoices': invoices
    })
        