from django.urls import path
from . import views

urlpatterns = [
     path('invoice/create/', views.create_invoice_view, name='create-invoice'),
]
