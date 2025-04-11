from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name    
    
class Invoice(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    billing_date = models.DateTimeField(auto_now_add=True)
    service_fee = models.DecimalField(max_digits=10, decimal_places=2)
    travel_expenses = models.DecimalField(max_digits=10, decimal_places=2)
    tax_percent = models.DecimalField(max_digits=5, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def calculate_total(self):
        subtotal = self.service_fee + self.travel_expenses
        tax = subtotal * (self.tax_percent / 100)
        return subtotal + tax
    
    def save(self, *args, **kwargs):
        self.total = self.calculate_total()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Invoice #{self.id} - {self.client.name}"

class Attachment(models.Model):
    invoice = models.ForeignKey('Invoice', on_delete=models.CASCADE, related_name='attachments')
    file = models.FileField(upload_to='attachments/')
    uploaded_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Attachment for Invoice #{self.invoice.id}"