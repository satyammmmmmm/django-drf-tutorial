from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hyderabad_jobs_view(request):
    s='<h1>hydera job information</h1>'
    return HttpResponse(s)
def banglore_jobs_view(request):
    s='<h1>banglore job information</h1>'
    return HttpResponse(s) 
def ncr_jobs_view(request):
    s='<h1>ncr job information</h1>'
    return HttpResponse(s)   