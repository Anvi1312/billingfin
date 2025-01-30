


from django.urls import path
from . import views
app_name = 'inventory'
urlpatterns = [
    path('print_added_stock/', views.print_inventory, name='print_inventory'),
    
    # path('order_pdf_template/', views.order_pdf_template, name='order_pdf_template'),
    path('order_pdf_template/', views.order_pdf_template, name='order_pdf_template'),

    path('dashboard/', views.inventory_dashboard, name='dashboard'),  # Ensure the URL is named 'dashboard'
    path('delete_medicine/<int:id>/', views.delete_medicine, name='delete_medicine'),  # Define the URL for deleting a medicine
    # path('add_medicine/', views.add_medicine, name='add_medicine'),  # Add this line for the add_medicine view
    # path('add/', views.add_medicine, name='add_medicine'),
    path('dashboard/update_stock/', views.update_stock, name='update_stock'),

    # path('inventory/', views.inventory_dashboard, name='inventory_dashboard'),  # Inventory dashboard
    path("inventory/add/", views.add_medicine, name="add_medicine"),  # Add medicine
    # path('inventory/edit/<int:medicine_id>/', views.edit_medicine, name='edit_medicine'),  # Edit medicine
    # path('inventory/delete/<int:medicine_id>/', views.delete_medicine, name='delete_medicine'),  # Delete medicine
    # Add other paths if needed
]
