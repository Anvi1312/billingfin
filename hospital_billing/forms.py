from django import forms
from .models import HospitalBill

class HospitalBillForm(forms.ModelForm):
    class Meta:
        model = HospitalBill
        fields = ['patient_name', 'doctor_name', 'service_description', 'charges', 'total_amount', 'gst_number', 'bill_date']
    
    bill_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))  # Ensures a date picker in the form

# class HospitalBillForm(forms.ModelForm):
#     class Meta:
#         model = HospitalBill
#         fields = ['patient_name', 'doctor_name', 'service_description', 'charges', 'total_amount', 'gst_number', 'bill_date']
#     bill_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))  # Ensures a date picker in the form


# # forms.py
# from django import forms
# from .models import HospitalBill, BillItem

# class HospitalBillForm(forms.ModelForm):
#     # Add any custom fields here as text input
#     patient = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Patient Name'}))
#     doctor = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Doctor Name'}))
#     gst_number = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter GST Number'}))
#     total_amount = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Total Amount'}))
#     bill_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Enter Bill Date', 'type': 'date'}))
    
#     class Meta:
#         model = HospitalBill
#         fields = ['patient', 'doctor', 'gst_number', 'total_amount', 'bill_date']

# class BillItemForm(forms.ModelForm):
#     medicine_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Medicine Name'}))
#     quantity = forms.IntegerField(min_value=1, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Quantity'}))
#     price_per_unit = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Price per Unit'}))
    
#     class Meta:
#         model = BillItem
#         fields = ['medicine_name', 'quantity', 'price_per_unit']




# # from django import forms
# # from .models import HospitalBill, BillItem, Patient, Service

# # # forms.py
# # from django import forms
# # from .models import HospitalBill

# # class HospitalBillForm(forms.ModelForm):
# #     class Meta:
# #         model = HospitalBill
# #         fields = ['patient', 'doctor', 'gst_number', 'total_amount', 'bill_date']

# # class HospitalBillDetailForm(forms.ModelForm):
# #     class Meta:
# #         model = HospitalBill
# #         fields = ['patient', 'doctor', 'gst_number', 'total_amount', 'bill_date']  # Add other fields as required


# # class BillItemForm(forms.ModelForm):
# #     class Meta:
# #         model = BillItem
# #         fields = ['service', 'quantity', 'rate']
# #         widgets = {
# #             'rate': forms.NumberInput(attrs={'step': '0.01'}),
# #         }

# # class HospitalBillDetailForm(forms.Form):
# #     # Patient Selection (Dropdown)
# #     patient = forms.ModelChoiceField(queryset=Patient.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    
# #     # Doctor Name and GST Number
# #     doctor_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
# #     gst_number = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
# #     # Bill Date
# #     bill_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))

# #     # Services (Dynamic Formset for Adding Multiple Items)
# #     items = forms.ModelMultipleChoiceField(queryset=Service.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
