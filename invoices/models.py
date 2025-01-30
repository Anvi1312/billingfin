from django.db import models
from django.core.exceptions import ValidationError


class Medicine(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

class Medicine(models.Model):
    name = models.CharField(max_length=200, unique=True)
    stock = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    def reduce_stock(self, quantity):
        if self.stock >= quantity:
            self.stock -= quantity
            self.save()
            return True
        else:
            return False

class Invoice(models.Model):
    customer_name = models.CharField(max_length=255)  # Make sure this field exists
    doctor_name = models.CharField(max_length=255)
    gst_number = models.CharField(max_length=255)
    bill_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)



# class Invoice(models.Model):
#     patient_name = models.CharField(max_length=200)
#     doctor_name = models.CharField(max_length=200)
#     gst_number = models.CharField(max_length=15)
#     bill_date = models.DateField(auto_now_add=True)
#     pharmacy_staff = models.CharField(max_length=100)
#     total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # This field must exist
#   # Renamed from 'total'
#     customer_name = models.CharField(max_length=200)  # Added customer_name field

    def __str__(self):
        return f"Invoice #{self.id} - {self.patient_name}"

class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name="items")
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def clean(self):
        if self.quantity > self.medicine.stock:
            raise ValidationError(f"Not enough stock for {self.medicine.name}. Available: {self.medicine.stock}")

    def save(self, *args, **kwargs):
        self.clean()
        self.medicine.stock -= self.quantity
        self.medicine.save()
        super().save(*args, **kwargs)

class PharmacyStaff(models.Model):
    name = models.CharField(max_length=200)
    employee_id = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name




# from django.db import models
# from django.core.exceptions import ValidationError
# from django.db import models

# class Medicine(models.Model):
#     name = models.CharField(max_length=200, unique=True)
#     stock = models.PositiveIntegerField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)

#     def __str__(self):
#         return self.name

#     def reduce_stock(self, quantity):
#         if self.stock >= quantity:
#             self.stock -= quantity
#             self.save()
#             return True
#         else:
#             return False

# class Invoice(models.Model):
#     patient_name = models.CharField(max_length=200)
#     doctor_name = models.CharField(max_length=200)
#     gst_number = models.CharField(max_length=15)
#     bill_date = models.DateField(auto_now_add=True)
#     pharmacy_staff = models.CharField(max_length=100)
#     total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

#     def __str__(self):
#         return f"Invoice #{self.id} - {self.patient_name}"

# class InvoiceItem(models.Model):
#     invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name="items")
#     medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     total = models.DecimalField(max_digits=10, decimal_places=2)

#     def clean(self):
#         if self.quantity > self.medicine.stock:
#             raise ValidationError(f"Not enough stock for {self.medicine.name}. Available: {self.medicine.stock}")

#     def save(self, *args, **kwargs):
#         self.clean()  
#         self.medicine.stock -= self.quantity  
#         self.medicine.save()  
#         super().save(*args, **kwargs)


# class PharmacyStaff(models.Model):
#     name = models.CharField(max_length=200)
#     employee_id = models.CharField(max_length=100, unique=True)

#     def __str__(self):
#         return self.name
