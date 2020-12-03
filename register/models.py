from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Employees(models.Model):
    Employee_ID = models.CharField(max_length=100)
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Date_Of_Birth = models.DateField(auto_now=False)
    Email = models.EmailField()
    phone_number = PhoneNumberField()
    Designation = models.TextField(max_length=100)


class Projects(models.Model):

    Project_ID = models.IntegerField()
    Project_Name = models.CharField(max_length=100)
    Project_Manager = models.CharField(max_length=100)
    Start_Date = models.DateField()
    End_Date = models.DateField()
