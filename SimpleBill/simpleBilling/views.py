from django.shortcuts import render

# Create your views here.
def create_invoice_view(request):
    return render(request, 'simpleBilling/invoice.html')

