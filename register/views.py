from django.shortcuts import render,redirect
from.models import Employees,Projects
from datetime import date 
from django.contrib import messages


# Create your views here.
def home(request):
        details = Employees.objects.all()
        return render(request,'home.html', {'details':  details})  

def employeeDetails(request,id):
        detail = Employees.objects.get(id=id)
        today = date.today()
        age = today.year - detail.dob.year
        if age==0:
                day = (today - detail.dob).days
                age = "{} Days".format(day) if day > 1 else "{} Day".format(day)
        elif age<0:
                age = 0

        projects = detail.projects.all()
        return render(request,'empDetails.html',{'detail' : detail,'age':age, 'projects': projects})


def employeeDetailForSearch(request):
        if Employees.objects.filter(firstName=request.GET['employeeName']).exists():
                detail = Employees.objects.get(firstName=request.GET['employeeName'])
                today = date.today()
                age = today.year - detail.dob.year
                if age==0:
                        day = (today - detail.dob).days
                        age = "{} Days".format(day) if day > 1 else "{} Day".format(day)
                elif age<0:
                        age = 0

                projects = detail.projects.all()
                return render(request,'empDetails.html',{'detail' : detail,'age':age, 'projects': projects})
        else:
                messages.info(request,'Please give the valid First Name')
                return redirect('home')



  
