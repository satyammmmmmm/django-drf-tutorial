from django.shortcuts import render
from testapp.models import emp
# Create your views here.
def empdata_view(request):
    emp_list =emp.objects.all()
    my_dict={'emp_list':emp_list}
    
    return render(request,'testapp/emp.html',my_dict)

