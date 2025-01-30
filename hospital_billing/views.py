from django.shortcuts import render, redirect
from .models import HospitalBill
from .forms import HospitalBillForm
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
from django.conf import settings

from django.utils import timezone

from django.shortcuts import render


from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import HospitalBillForm
from .models import HospitalBill
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO



from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import HospitalBillForm
# from .utils import generate_pdf  # Assuming you have a function for generating PDFs
import os
from django.conf import settings

from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
from .forms import HospitalBillForm


def generate_pdf(bill_data):
    """
    Generates a PDF from the given bill data.
    """
    # Render the HTML content using the form data
    html_content = render_to_string('hospital_billing/bill_pdf.html', {'bill_data': bill_data})
    html = HTML(string=html_content)
    
    # Generate PDF from the HTML string
    pdf_file = html.write_pdf()
    return pdf_file

def create_bill(request):
    """
    Handles the form submission to generate and download a hospital bill PDF.
    """
    if request.method == 'POST':
        form = HospitalBillForm(request.POST)
        
        if form.is_valid():
            # Get cleaned form data
            bill_data = form.cleaned_data
            
            # Generate the PDF
            pdf_content = generate_pdf(bill_data)
            
            # Prepare the HTTP response to download the PDF
            response = HttpResponse(pdf_content, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="generated_bill.pdf"'
            return response
        
        else:
            # If the form is not valid, just render it again with errors
            return render(request, 'hospital_billing/create_bill.html', {'form': form})

    else:
        # If it's not a POST request, just display an empty form
        form = HospitalBillForm()
        return render(request, 'hospital_billing/create_bill.html', {'form': form})

# def generate_pdf(bill_data):
#     """
#     Generates a PDF file from the given data.
#     """
#     # Render HTML from template
#     html_content = render_to_string('hospital_billing/bill_template.html', {'bill_data': bill_data})
#     html = HTML(string=html_content)
    
#     # Generate the PDF
#     pdf_file = html.write_pdf()
#     return pdf_file

# def bill_success(request):
#     if request.method == 'POST':
#         form = HospitalBillForm(request.POST)
#         if form.is_valid():
#             # Get cleaned data from the form
#             bill_data = form.cleaned_data

#             # Generate the PDF on the fly
#             pdf_content = generate_pdf(bill_data)

#             # Create the response to send the PDF as a downloadable file
#             response = HttpResponse(pdf_content, content_type='application/pdf')
#             response['Content-Disposition'] = 'attachment; filename="generated_bill.pdf"'
#             return response
#         else:
#             # If the form is invalid, you can return the form again with error messages
#             return render(request, 'hospital_billing/create_bill.html', {'form': form})
#     else:
#         form = HospitalBillForm()
#         return render(request, 'hospital_billing/create_bill.html', {'form': form})

# def bill_success(request):
#     # Assuming the PDF is generated and saved on the server
#     file_path = os.path.join(settings.MEDIA_ROOT, 'generated_bill.pdf')

#     # Ensure the file exists before sending it
#     if os.path.exists(file_path):
#         with open(file_path, 'rb') as pdf:
#             response = HttpResponse(pdf.read(), content_type='application/pdf')
#             response['Content-Disposition'] = 'attachment; filename="generated_bill.pdf"'
#             return response
#     else:
#         # If no file found, you can redirect or render a custom error message
#         return render(request, 'hospital_billing/bill_error.html')
# # def bill_success(request):

    
#     return render(request, 'hospital_billing/bill_success.html')  # Create a simple success template


# def generate_pdf(bill):
#     # Create an in-memory buffer for the PDF
#     buffer = BytesIO()
    
#     # Create a PDF canvas
#     p = canvas.Canvas(buffer, pagesize=letter)
    
#     # Add content to the PDF
#     p.drawString(100, 750, f"Hospital Bill for {bill.patient_name}")
#     p.drawString(100, 730, f"Doctor: {bill.doctor_name}")
#     p.drawString(100, 710, f"Services: {bill.service_description}")
#     p.drawString(100, 690, f"Charges: {bill.charges}")
#     p.drawString(100, 670, f"GST Number: {bill.gst_number}")
#     p.drawString(100, 650, f"Total Amount: {bill.total_amount}")
#     p.drawString(100, 630, f"Bill Date: {bill.bill_date}")
    
#     # End the PDF document
#     p.showPage()
#     p.save()

#     # Get the value of the buffer and return it as an HTTP response
#     buffer.seek(0)
#     return buffer



# def create_bill(request):
#     if request.method == "POST":
#         form = HospitalBillForm(request.POST)
#         if form.is_valid():
#             bill = form.save(commit=False)
#             bill.total_amount = bill.charges  # Assuming the total amount is the same as charges for now
#             bill.save()
#             return redirect('hospital_billing:bill_success')
#     else:
#         form = HospitalBillForm()

#     return render(request, 'hospital_billing/create_bill.html', {'form': form})



# def generate_pdf(request, bill_id):
#     bill = HospitalBill.objects.get(id=bill_id)
#     html_content = render_to_string('hospital_billing/bill_pdf.html', {'bill': bill})
#     pdf = HTML(string=html_content).write_pdf()

#     response = HttpResponse(pdf, content_type='application/pdf')
#     response['Content-Disposition'] = f'inline; filename="bill_{bill_id}.pdf"'
#     return response
# from .forms import HospitalBillDetailForm  # Make sure this import is correct

# def create_bill(request):
#     if request.method == 'POST':
#         bill_form = HospitalBillForm(request.POST)
#         if bill_form.is_valid():
#             # Manually assign the patient using the provided name
#             patient_name = bill_form.cleaned_data['patient']
#             try:
#                 patient = Patient.objects.get(name=patient_name)
#                 hospital_bill = bill_form.save(commit=False)
#                 hospital_bill.patient = patient  # Set the actual Patient instance
#                 hospital_bill.save()

#                 # Handle BillItems (medicines)
#                 bill_item_form = BillItemForm(request.POST)
#                 if bill_item_form.is_valid():
#                     bill_item = bill_item_form.save(commit=False)
#                     bill_item.bill = hospital_bill
#                     bill_item.save()

#                 return redirect('some_success_url')  # Redirect after saving
#             except Patient.DoesNotExist:
#                 bill_form.add_error('patient', 'Patient does not exist.')

#     else:
#         bill_form = HospitalBillForm()
#         bill_item_form = BillItemForm()

#     return render(request, 'hospital_billing/create_bill.html', {
#         'bill_form': bill_form,
#         'bill_item_form': bill_item_form,
#     })

# def create_bill(request):
#     if request.method == 'POST':
#         bill_form = HospitalBillForm(request.POST)
#         if bill_form.is_valid():
#             # Save the HospitalBill
#             hospital_bill = bill_form.save()
#             # Handle the BillItems (medicine)
#             bill_item_form = BillItemForm(request.POST)
#             if bill_item_form.is_valid():
#                 bill_item = bill_item_form.save(commit=False)
#                 bill_item.bill = hospital_bill
#                 bill_item.save()
#             return redirect('some_success_url')  # Redirect after saving
#     else:
#         bill_form = HospitalBillForm()
#         bill_item_form = BillItemForm()

#     return render(request, 'hospital_billing/create_bill.html', {
#         'bill_form': bill_form,
#         'bill_item_form': bill_item_form,
#     })


# def create_bill(request):
#     if request.method == 'POST':
#         form = HospitalBillDetailForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('some_success_url')  # Redirect after successful form submission
#     else:
#         form = HospitalBillDetailForm()

#     return render(request, 'hospital_billing/create_bill.html', {'form': form})


# def create_bill(request):
#     if request.method == 'POST':
#         form = HospitalBillDetailForm(request.POST)
#         if form.is_valid():
#             # Create a new instance of HospitalBill without saving yet
#             hospital_bill = form.save(commit=False)
#             # Set the current date and time for the bill_date
#             hospital_bill.bill_date = timezone.now()  # Set current date and time
#             # Save the hospital_bill after setting the bill_date
#             hospital_bill.save()
#             return redirect('bill_success')  # Redirect after submission
#     else:
#         form = HospitalBillDetailForm()

#     return render(request, 'hospital_billing/index.html', {'form': form})


# def create_bill(request):
#     if request.method == 'POST':
#         bill_form = HospitalBillForm(request.POST)
#         if bill_form.is_valid():
#             bill = bill_form.save()

#             # Redirect to add items to the bill
#             return redirect('add_items', bill_id=bill.id)
#     else:
#         bill_form = HospitalBillForm()

# #     return render(request, 'hospital_billing/create_bill.html', {'form': bill_form})

# def add_items(request, bill_id):
#     bill = HospitalBill.objects.get(id=bill_id)
#     services = Service.objects.all()

#     if request.method == 'POST':
#         for service_id in request.POST.getlist('service'):
#             quantity = int(request.POST.get(f'quantity_{service_id}'))
#             service = Service.objects.get(id=service_id)
#             BillItem.objects.create(bill=bill, service=service, quantity=quantity)

#         # Calculate total bill amount
#         bill.total_amount = sum(item.total_price for item in bill.billitem_set.all())
#         bill.save()

#         # Generate the PDF
#         return generate_pdf(request, bill.id)

#     return render(request, 'hospital_billing/add_items.html', {'bill': bill, 'services': services})

# def generate_pdf(request, bill_id):
#     bill = HospitalBill.objects.get(id=bill_id)
#     html = render_to_string('hospital_billing/bill_pdf.html', {'bill': bill})

#     # Create PDF from HTML
#     pdf_file = HTML(string=html).write_pdf()

#     # Return PDF as response
#     response = HttpResponse(pdf_file, content_type='application/pdf')
#     response['Content-Disposition'] = f'attachment; filename="bill_{bill.id}.pdf"'
#     return response
