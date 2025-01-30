from django import forms
from .models import Medicine, Category


class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['name', 'category', 'price', 'quantity', 'description', 'expiry_date', 'manufacturer']



class UpdateStockForm(forms.ModelForm):
    action = forms.ChoiceField(choices=[('add', 'Add Stock'), ('reduce', 'Reduce Stock')], label='Action')

    class Meta:
        model = Medicine
        fields = ['name', 'category', 'price', 'quantity', 'description', 'expiry_date', 'manufacturer']

    # Custom validation for quantity and action
    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity <= 0:
            raise forms.ValidationError("Quantity should be a positive number.")
        return quantity

    def clean_action(self):
        action = self.cleaned_data.get('action')
        if action not in ['add', 'reduce']:
            raise forms.ValidationError("Invalid action selected.")
        return action




class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']