from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def gettime(request):
    time=datetime.datetime.now()
    s='<h1> hello '+str(time)+'</h1>'
    return HttpResponse(s) 
