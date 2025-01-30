# from django.urls import path
# from . import views

# urlpatterns = [
#     # Add this path for the hospital billing landing page
#     path('', views.create_bill, name='hospital_billing_index'),  # Home or landing page of the billing app
#     path('create_bill/', views.create_bill, name='create_bill'),
#     path('add_items/<int:bill_id>/', views.add_items, name='add_items'),
#     path('generate_pdf/<int:bill_id>/', views.generate_pdf, name='generate_pdf'),
# ]


from django.urls import path
from . import views

app_name = 'hospital_billing'  # Ensure this line is present


urlpatterns = [
    path('', views.create_bill, name='create_bill'),
    path('', views.create_bill, name='create_bill'),
    # path('success/', views.bill_success, name='bill_success'),  # Add this line
    # path('bill_success/', views.bill_success, name='bill_success'),  # Add the success page route

    path('generate_pdf/<int:bill_id>/', views.generate_pdf, name='generate_pdf'),
]
