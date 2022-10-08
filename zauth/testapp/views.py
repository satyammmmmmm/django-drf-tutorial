from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from testapp.forms import SignUpForm
from django.http import HttpResponseRedirect
# Create your views here.
def homepageview(request):
    return render(request,'testapp/base.html')

@login_required
def javapageview(request):
    return render(request,'testapp/java.html')

def pythonpageview(request):
    return render(request,'testapp/python.html')

def logoutview(request):
    return render(request,'testapp/logout.html')

def signupview(request):
    form=SignUpForm()
    if request.method=="POST":
        form=SignUpForm(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'testapp/signup.html',{'form':form})
    
