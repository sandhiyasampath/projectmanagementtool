from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Projects(models.Model):
    Project = models.CharField(max_length=100)

    def __str__(self):
        return self.Project


class Employees(models.Model):
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Date_Of_Birth = models.DateField()
    Email = models.EmailField()
    phone_number = PhoneNumberField()
    Designation = models.CharField(max_length=100)
    Employees_projects = models.ManyToManyField(Projects)

    def __str__(self):
        return self.First_Name





