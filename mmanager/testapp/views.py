from django.shortcuts import render
from testapp.models import Employee
from django.shortcuts import render

# Create your views here.
def display(request):
    emp_list=Employee.objects.getempsal(15000,30000)
    #emp_list=Employee.objects.all()
    return render(request,'testapp/index.html',{'emp_list':emp_list})