from django.db import models

# Create your models here.
class PhoneDevice(models.Model):
    brand = models.CharField(max_length=100)
    model_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return f"{self.brand} {self.model_name}"