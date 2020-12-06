from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Projects(models.Model):
    projectName = models.CharField(max_length=100)
    startDate = models.DateField(auto_now=True)
    endDate = models.DateField()

    def __str__(self):
        return self.projectName


class Employees(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    dob = models.DateField()
    email = models.EmailField()
    phoneNumber = PhoneNumberField()
    designation = models.CharField(max_length=100)
    projects = models.ManyToManyField(Projects)

    def __str__(self):
        return self.firstName





