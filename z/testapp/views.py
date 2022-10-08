from django.shortcuts import render,redirect
from testapp.models import Employee

# Create your views here.
def retrieve(request):
    emp_list=Employee.objects.all()
    return render(request,'testapp/a.html',{'emp_list':emp_list})
from testapp.forms import Employeeform
def create(request):
    form=Employeeform() 
    if request.method=="POST":
        form=Employeeform(request.POST)
        form.save()
        return redirect('/')
        
    return render(request,'testapp/insert.html',{'form':form})

def delete(request,id):
    employee=Employee.objects.get(id=id)
    employee.delete()
    return redirect('/')
def update(request,id):
    employee=Employee.objects.get(id=id)
    form=Employeeform(instance=employee)
    if request.method=="POST":
        form=Employeeform(request.POST,instance=employee)
        form.save()
        return redirect('/')
    return render(request,'testapp/update.html',{'form':form})


# Create your views here.
