from django.shortcuts import render,redirect
from.models import Employees,Projects
from datetime import date 


# Create your views here.
def home(request):
        details = Employees.objects.all()
        return render(request,'home.html', {'details':  details})  

def employeeDetails(request,id):
        detail = Employees.objects.get(id=id)
        today = date.today() 
        age = (today.year - detail.dob.year - ((today.month, today.day) < (detail.dob.month, detail.dob.day)))
        projects = detail.projects.all() 
        return render(request,'empDetails.html',{'detail' : detail,'age':age, 'projects': projects})


  
