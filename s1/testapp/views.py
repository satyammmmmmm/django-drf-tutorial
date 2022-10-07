from django.shortcuts import render

from testapp.forms import *
# Create your views here.
def nameview(request):
    form=NameForm()
    return render(request,'testapp/name.html',{'form':form})

def ageview(request):
    name=request.GET['name']
    request.session['name']=name 
    form=AgeForm()
    return render(request,'testapp/age.html',{'form':form,'name':name})