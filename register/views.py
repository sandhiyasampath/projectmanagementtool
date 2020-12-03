from django.shortcuts import render,redirect
from.models import Employees,Projects
# Create your views here.
def home(request):
        details = Employees.objects.all()
        return render(request,'home.html', {'details':  details})  

def employeeDetails(request,id):
        detail = Employees.objects.get(Employee_ID=id)
        print(detail.phone_number)
        return render(request,'empDetails.html',{'detail' : detail})