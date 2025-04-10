from django.shortcuts import render
from .models import Client, Invoice, Attachment

# Create your views here.
def create_invoice_view(request):
    return render(request, 'simpleBilling/invoice.html')

def create_invoice_view(request):
    if request.method == 'POST':
        client_name = request.POST.get('client_name')
        service_fee = request.POST.get('service_fee')
        travel_expenses = request.POST.get('travel_expenses')
        tax_percent = request.POST.get('tax_percent')
        uploaded_files = request.FILES.getlist('attachments')
        
        client,
        
