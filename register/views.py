from django.shortcuts import render,redirect
from.models import Employees,Projects
from datetime import date 


# Create your views here.
def home(request):
        details = Employees.objects.all()
        return render(request,'home.html', {'details':  details})  

def employeeDetails(request,id):
        detail = Employees.objects.get(Employee_ID=id)
        today = date.today() 
        age = (today.year - detail.Date_Of_Birth.year - ((today.month, today.day) < (detail.Date_Of_Birth.month, detail.Date_Of_Birth.day)))
        projects = detail.Employees_projects.all()
        print([projects])
 

        return render(request,'empDetails.html',{'detail' : detail,'age':age, 'projects': projects})


  
