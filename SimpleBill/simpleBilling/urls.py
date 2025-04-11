from django.urls import path
from . import views

urlpatterns = [
     path('', views.invoice_list_create_view, name="home"),
     path('invoice/create/', views.create_invoice_view, name='create-invoice'),
     path('invoice/success/', views.invoice_success_view, name='invoice-success'),
     path('invoice/<int:invoice_id>/edit/', views.edit_invoice_view, name="edit-invoice"),
     path('invoice/<int:invoice_id>/delete', views.delete_invoice_view, name="delete-invoice"),
]
