# forms.py (in the Invoices app)
from django import forms
from inventory.models import Medicine
from .models import InvoiceItem

class InvoiceItemForm(forms.ModelForm):
    class Meta:
        model = InvoiceItem
        fields = ['medicine', 'quantity', 'price']
    
    medicine = forms.ModelChoiceField(queryset=Medicine.objects.all(), empty_label="Select Medicine")
    price = forms.DecimalField(required=False, widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        super(InvoiceItemForm, self).__init__(*args, **kwargs)
        if 'medicine' in self.data:
            try:
                medicine_id = int(self.data.get('medicine'))
                medicine = Medicine.objects.get(id=medicine_id)
                self.fields['price'].initial = medicine.price
            except (ValueError, TypeError, Medicine.DoesNotExist):
                pass
# invoices/forms.py
from django import forms
from .models import Invoice

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['customer_name', 'total_amount'] # include your required fields here


# from django import forms
# from .models import Invoice, InvoiceItem, Medicine

# class InvoiceForm(forms.ModelForm):
#     class Meta:
#         model = Invoice
#         fields = ['patient_name', 'doctor_name', 'gst_number', 'pharmacy_staff']

# class InvoiceItemForm(forms.ModelForm):
#     medicine = forms.ModelChoiceField(queryset=Medicine.objects.all(), empty_label="Select Medicine")

#     class Meta:
#         model = InvoiceItem
#         fields = ['medicine', 'quantity']

#     def clean_quantity(self):
#         quantity = self.cleaned_data['quantity']
#         medicine = self.cleaned_data.get('medicine')

#         if medicine and quantity > medicine.stock:
#             raise forms.ValidationError(f"Only {medicine.stock} left in stock for {medicine.name}.")

#         return quantity
