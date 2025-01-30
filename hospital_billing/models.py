
from django.db import models

class HospitalBill(models.Model):
    patient_name = models.CharField(max_length=100)  # Patient name as text input
    doctor_name = models.CharField(max_length=100)  # Doctor name as text input
    service_description = models.TextField()  # Description of services provided
    charges = models.DecimalField(max_digits=10, decimal_places=2)  # Charges for the service
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)  # Total bill amount
    gst_number = models.CharField(max_length=15)  # GST number
    bill_date = models.DateField()  # Simple DateField for user input

    def __str__(self):
        return f"Bill for {self.patient_name} on {self.bill_date}"

# from django.db import models
# from django.contrib.auth.models import User
# from django.utils import timezone


# class Patient(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     dob = models.DateField()
#     contact_number = models.CharField(max_length=15)
#     email = models.EmailField()

#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"

# class Service(models.Model):
#     name = models.CharField(max_length=255)
#     price = models.DecimalField(max_digits=10, decimal_places=2)

#     def __str__(self):
#         return self.name

# class HospitalBill(models.Model):
    
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
#     doctor = models.CharField(max_length=100)  # Example: Doctor name field (adjust as necessary)
#     gst_number = models.CharField(max_length=15)
#     bill_date = models.DateTimeField(default=timezone.now)  # Automatically set the current date and time
#     total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

#     def __str__(self):
#         return f"Bill for {self.patient} on {self.bill_date}"

# class BillItem(models.Model):
#     bill = models.ForeignKey(HospitalBill, related_name="items", on_delete=models.CASCADE)
#     service = models.ForeignKey(Service, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField()
#     rate = models.DecimalField(max_digits=10, decimal_places=2)
#     total = models.DecimalField(max_digits=10, decimal_places=2)

#     def save(self, *args, **kwargs):
#         self.total = self.quantity * self.rate
#         super().save(*args, **kwargs)


# # from django.db import models

# # class Patient(models.Model):
# #     first_name = models.CharField(max_length=100)
# #     last_name = models.CharField(max_length=100)
# #     dob = models.DateField()
# #     contact_number = models.CharField(max_length=15)
# #     email = models.EmailField()

# #     def __str__(self):
# #         return f"{self.first_name} {self.last_name}"

# # class Service(models.Model):
# #     name = models.CharField(max_length=200)
# #     price = models.DecimalField(max_digits=10, decimal_places=2)

# #     def __str__(self):
# #         return self.name

# # class HospitalBill(models.Model):
# #     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
# #     bill_date = models.DateField(auto_now_add=True)
# #     total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
# #     def __str__(self):
# #         return f"Bill for {self.patient} on {self.bill_date}"

# # class BillItem(models.Model):
# #     bill = models.ForeignKey(HospitalBill, on_delete=models.CASCADE)
# #     service = models.ForeignKey(Service, on_delete=models.CASCADE)
# #     quantity = models.PositiveIntegerField()
# #     total_price = models.DecimalField(max_digits=10, decimal_places=2)

# #     def save(self, *args, **kwargs):
# #         self.total_price = self.service.price * self.quantity
# #         super().save(*args, **kwargs)
