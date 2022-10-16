from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def welcome(request):
    print('view called')
    return HttpResponse('<h1> custo middleware</h1>')