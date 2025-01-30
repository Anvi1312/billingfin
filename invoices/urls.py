from django.urls import path
from .views import invoice_create, generate_invoice, print_invoice, get_medicine_price, invoice_success


urlpatterns = [
    path('', invoice_create, name='invoice_create'),
    path('generate_invoice/', generate_invoice, name='generate_invoice'),
    path('inventory/',invoice_create, name='inventory_dashboard'),
    path('print_invoice/<int:invoice_id>/', print_invoice, name='print_invoice'),  # Added this line for invoice printing
    path('get_medicine_price/', get_medicine_price, name='get_medicine_price'),  # Added this line for getting medicine price
    path('invoice_success/', invoice_success, name='invoice_success'),

]
