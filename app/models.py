from django.db import models

# Create your models here.
class Clinic(models.Model):
    name = models.CharField(max_length=400)
    number_of_patients = models.IntegerField()
    country = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    address = models.CharField(max_length=250)
    zip_code = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=15)