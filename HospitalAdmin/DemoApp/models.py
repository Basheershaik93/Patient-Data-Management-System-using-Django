from django.db import models


# Create your models here.
class Patient(models.Model):
    PatientId=models.CharField(max_length=20,primary_key=True)
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    Gender=models.CharField(max_length=15)
    Email=models.CharField(max_length=100)
    Address=models.CharField(max_length=50)
    Description=models.CharField(max_length=100)
    PaymentType=models.CharField(max_length=15)
    Acceptance=models.CharField(max_length=15)
    


class Invoice(models.Model):
    patient = models.CharField(max_length=20)
    date = models.DateField(auto_now_add=True)
    medicine_name= models.CharField(max_length=100)
    quantity = models.IntegerField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)



