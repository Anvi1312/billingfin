# inventory/models.py
from django.db import models
from datetime import date

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Medicine(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)  # Change category to CharField
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=0)
    description = models.TextField(default="No description provided")
    expiry_date = models.DateField(default=date.today)
    manufacturer = models.CharField(max_length=255, default="Unknown")

    def __str__(self):
        return self.name



