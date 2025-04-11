from django.shortcuts import render, redirect
from .models import Client, Invoice, Attachment
from decimal import Decimal
from .forms import InvoiceForm

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
    form = InvoiceForm(request.POST or None)
    invoices = Invoice.objects.all()
    
    if request.method == 'POST':
        if form.is_valid():
            invoice = form.save()
            
            uploaded_files = request.FILES.getlist('attachments')
            for file in uploaded_files:
                Attachment.objects.create(invoice=invoice, file=file)
            
            return redirect('invoice-success')
        
    context = {
        'form': form,
        'invoices': invoices,
    }
    return render(request, 'simpleBilling/invoice.html', context)