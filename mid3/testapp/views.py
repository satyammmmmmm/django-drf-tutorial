from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    print(10/0)
    return HttpResponse('<h1>from vieew</h1>')