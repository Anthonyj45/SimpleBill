from django.contrib import admin
from .models import Client, Invoice, Attachment

# Register your models here.
admin.site.register(Client)
admin.site.register(Invoice)
admin.site.register(Attachment)