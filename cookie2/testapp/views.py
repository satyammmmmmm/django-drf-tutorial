import datetime
from django.shortcuts import render
from testapp.forms import loginform
# Create your views here.
def home(request):
    form=loginform()
    return render(request,'testapp/home.html',{'form':form})
def datetime(request):
    name=request.GET['name']
    
  #  date_time=datetime.datetime.now()
    response=render(request,'testapp/datetime.html',{'name':name})
    response.set_cookie('name',name)
    return response