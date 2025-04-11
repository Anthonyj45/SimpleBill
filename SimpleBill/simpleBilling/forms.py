from django import forms 
from .models import Invoice

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['client', 'service_fee', 'travel_expenses', 'tax_percent', 'notes']