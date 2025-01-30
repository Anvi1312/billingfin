from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Medicine, Category
from inventory.models import Medicine
from datetime import datetime  # Add this import at the top
from django.contrib import messages

from django.template.loader import get_template
from xhtml2pdf import pisa
from django.http import HttpResponse
from .models import Medicine


# inventory/views.py
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from .models import Medicine


# inventory/views.py
from django.shortcuts import render
from .models import Medicine
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from .models import Medicine, Category


# inventory/views.py
from django.shortcuts import render
from .models import Medicine
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


from django.shortcuts import render, redirect
from .forms import UpdateStockForm
from .models import Medicine
from django.template.loader import render_to_string
from weasyprint import HTML
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

from django.shortcuts import render, redirect
from .forms import UpdateStockForm
from .models import Medicine
from django.template.loader import render_to_string
from weasyprint import HTML
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)



def order_pdf_template(request): #this prints the current inventory but not the details are avaliable
    if request.method == 'POST':
        # Debugging: Print all POST data to check if 'name' is present
        # logging.debug(f"POST Data: {request.POST}")

        # Extract form data from the POST request
        name = request.POST.get('name')
        category = request.POST.get('category')  # Now it's a text field
        price = request.POST.get('price')
        description = request.POST.get('description')
        manufacturer = request.POST.get('manufacturer')
        quantity = request.POST.get('quantity')
        expiry_date = request.POST.get('expiry_date')

        # Check if required fields are missing and log them
        if not name:
            # logging.error("Name field is missing in POST data")
            return HttpResponse("Name field is missing", status=400)
        
        # Create a new Medicine instance
        medicine = Medicine(
            name=name,
            category=category,
            price=price,
            description=description,
            manufacturer=manufacturer,
            quantity=quantity,
            expiry_date=expiry_date
        )
        medicine.save()  # Save to database

        # Prepare data for the template
        context = {
            'medicine': medicine,
        }

        # Load the template for rendering the PDF
        template = get_template('inventory/order_pdf_template.html')
        html = template.render(context)

        # Generate PDF from HTML
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="added_medicine_inventory.pdf"'

        pisa_status = pisa.CreatePDF(html, dest=response)
        
        if pisa_status.err:
            return HttpResponse('Error generating PDF', status=500)
        
        return response
    
    return HttpResponse("Invalid request", status=400)



def print_inventory(request):
    if request.method == 'POST':
        # Fetch all medicines from the database
        medicines = Medicine.objects.all()  # Fetch all medicines from the database

        # Prepare data for the PDF rendering
        context = {
            'medicines': medicines,  # Pass the medicines data to the template
        }

        # Load the inventory PDF template
        template = get_template('inventory/inventory_pdf.html')
        html = template.render(context)

        # Create the HTTP response for PDF generation
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="inventory_report.pdf"'

        # Use xhtml2pdf to convert HTML to PDF and send the response
        pisa_status = pisa.CreatePDF(html, dest=response)

        # Check for errors during the PDF generation process
        if pisa_status.err:
            return HttpResponse('We encountered some errors generating your PDF.')

        return response

    return HttpResponse("Invalid request", status=400)

# def print_added_stock(request):
#     if request.method == 'POST':
#         # Fetch the medicine details entered in the form
#         medicine_name = request.POST.get('name')
#         category = request.POST.get('category')
#         manufacturer = request.POST.get('manufacturer')
#         description = request.POST.get('description')
#         price = request.POST.get('price')
#         quantity = request.POST.get('quantity')
#         expiry_date = request.POST.get('expiry_date')

#         # Create a new Medicine entry in the database
#         new_medicine = Medicine(
#             name=medicine_name,
#             category=category,
#             manufacturer=manufacturer,
#             description=description,
#             price=price,
#             quantity=quantity,
#             expiry_date=expiry_date
#         )
#         new_medicine.save()

#         # Prepare the data to be rendered in the PDF
#         context = {
#             'medicine': new_medicine,
#         }

#         # Render the template with the medicine data
#         template = get_template('inventory/order_pdf_template.html')
#         html = template.render(context)

#         # Create PDF from the HTML
#         response = HttpResponse(content_type='application/pdf')
#         response['Content-Disposition'] = 'attachment; filename="order_report.pdf"'
#         pisa_status = pisa.CreatePDF(html, dest=response)

#         if pisa_status.err:
#             return HttpResponse('We had some errors generating your PDF.')

#         return response

#     return HttpResponse("Invalid request", status=400)


# def print_inventory(request):
#     if request.method == 'POST':
#         # Fetch medicines from the database
#         medicines = Medicine.objects.all()  # Fetch all medicines

#         # Prepare data for rendering the PDF
#         context = {
#             'medicines': medicines,
#         }

#         # Get the template for the order PDF (make sure your template is set up correctly)
#         template = get_template('inventory/inventory_pdf.html')
#         html = template.render(context)

#         # Convert HTML to PDF
#         response = HttpResponse(content_type='application/pdf')
#         response['Content-Disposition'] = 'attachment; filename="inventory_report.pdf"'
        
#         # Use BytesIO to generate the PDF
#         pisa_status = pisa.CreatePDF(html, dest=response)

#         # Check if there are any errors in PDF generation
#         if pisa_status.err:
#             return HttpResponse('We had some errors generating your PDF.')

#         return response

#     return HttpResponse("Invalid request", status=400)




# def print_inventory(request):
#     if request.method == 'POST':
#         # Fetch medicines from the database
#         medicines = Medicine.objects.all()  # Make sure it's fetching the medicine as text field category

#         # Prepare data for rendering the PDF
#         context = {
#             'medicines': medicines,
#         }

#         # Get the template for the order PDF
#         template = get_template('inventory/inventory_pdf.html')
#         html = template.render(context)

#         # Convert HTML to PDF
#         response = HttpResponse(content_type='application/pdf')
#         response['Content-Disposition'] = 'attachment; filename="order_report.pdf"'
#         pisa_status = pisa.CreatePDF(html, dest=response)

#         if pisa_status.err:
#             return HttpResponse('We had some errors generating your PDF.')

#         return response

#     return HttpResponse("Invalid request", status=400)





def update_stock(request):
    if request.method == 'POST':
        form = UpdateStockForm(request.POST)
        if form.is_valid():
            # Get the form data
            medicine_name = form.cleaned_data['name']
            quantity = form.cleaned_data['quantity']
            action = form.cleaned_data['action']
            category = form.cleaned_data['category']
            price = form.cleaned_data['price']
            description = form.cleaned_data['description']
            expiry_date = form.cleaned_data['expiry_date']
            manufacturer = form.cleaned_data['manufacturer']

            # Check if the medicine exists
            medicine, created = Medicine.objects.get_or_create(
                name=medicine_name,
                defaults={
                    'category': category,
                    'price': price,
                    'description': description,
                    'expiry_date': expiry_date,
                    'manufacturer': manufacturer
                }
            )

            # Update the quantity based on the action
            if action == 'add':
                medicine.quantity += quantity
            elif action == 'reduce':
                if medicine.quantity >= quantity:
                    medicine.quantity -= quantity
                else:
                    logger.error("Not enough stock to reduce.")
                    return render(request, 'inventory/update_stock.html', {'form': form, 'error': 'Not enough stock to reduce.'})

            # Save the updated medicine
            medicine.save()

            # Generate PDF after the stock update
            pdf_content = render_to_string('inventory/update_stock_pdf.html', {'medicine': medicine})
            pdf_file = HTML(string=pdf_content).write_pdf()

            response = HttpResponse(pdf_file, content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{medicine.name}_invoice.pdf"'

            return response  # Return the PDF as a downloadable response

    else:
        form = UpdateStockForm()

    return render(request, 'inventory/update_stock.html', {'form': form})


def generate_pdf_invoice(medicine):
    # Create a file-like buffer to receive PDF data
    buffer = BytesIO()

    # Create a canvas to generate PDF
    p = canvas.Canvas(buffer, pagesize=letter)
    p.drawString(100, 750, f"Medicine: {medicine.name}")
    p.drawString(100, 735, f"Category: {medicine.category}")
    p.drawString(100, 720, f"Price: ₹{medicine.price}")
    p.drawString(100, 705, f"Description: {medicine.description}")
    p.drawString(100, 690, f"Quantity: {medicine.quantity}")
    p.drawString(100, 675, f"Expiry Date: {medicine.expiry_date}")

    # Finalize the PDF
    p.showPage()
    p.save()

    # Get PDF data from buffer
    pdf = buffer.getvalue()
    buffer.close()

    # Return the PDF as an HttpResponse
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{medicine.name}_invoice.pdf"'
    return response

def delete_medicine(request, id):
    # Fetch the medicine object by its ID
    try:
        medicine = Medicine.objects.get(id=id)
        medicine.delete()  # Delete the medicine from the database
        print(f"Medicine deleted: {medicine.name}")
    except Medicine.DoesNotExist:
        print("Medicine not found.")
    
    return redirect('inventory:dashboard') 



def add_medicine(request):
    # Fetch all medicines and categories from the database to display in the form
    medicines = Medicine.objects.all()  
    categories = Category.objects.all()  

    if request.method == 'POST':
        # Get the data from the form
        name = request.POST.get('name')
        # category = request.POST.get('category')  # Should be a text field now
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        description = request.POST.get('description')
        expiry_date = request.POST.get('expiry_date')
        manufacturer = request.POST.get('manufacturer')

        # Check if all the necessary fields are provided
        if not name or not price or not quantity or not category:
            messages.error(request, "All fields are required.")
            return render(request, 'add_medicine.html', {'medicines': medicines, 'categories': categories})

        # Create a new Medicine instance
        medicine = Medicine(
            name=name,
            # category=category.objects.get(id=category),
            price=price,
            quantity=quantity,
            description=description,
            expiry_date=expiry_date,
            manufacturer=manufacturer
        )
        
        # Save the medicine to the database
        medicine.save()

        # Success message
        messages.success(request, f"Medicine '{name}' added successfully!")
        
        # Redirect to the inventory dashboard (or wherever you want)
        return redirect('inventory:dashboard')

    return render(request, 'add_medicine.html', {'medicines': medicines, 'categories': categories})



def inventory_dashboard(request):
    medicines = Medicine.objects.all()  # Fetch all medicines from the database
    categories = Category.objects.all()  # Fetch all categories if needed
    total_medicines = medicines.count()
    low_stock_medicines = medicines.filter(quantity__lt=5).count()
    out_of_stock = medicines.filter(quantity=0).count()

    context = {
        'medicines': medicines,
        'total_medicines': total_medicines,
        'low_stock_medicines': low_stock_medicines,
        'out_of_stock': out_of_stock,
    }

    return render(request, 'inventory/dashboard.html', context)







