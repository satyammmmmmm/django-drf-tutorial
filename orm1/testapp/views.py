from django.shortcuts import render
from testapp.models import Employee
from django.db.models import Q
# Create your views here.
def retrieve_view(request):
    
     #emp_list=Employee.objects.exclude(esal__gt=15000) & Employee.objects.exclude(ename__istartswith='P')
   # emp_list=Employee.objects.filter(Q(ename__startswith='P') & Q(esal__gt=15000))
     emp_list=Employee.objects.all().values_list('ename','eaddr')
     return render(request,'testapp/base.html',{'emp_list':emp_list})
