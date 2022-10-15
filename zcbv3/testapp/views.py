from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView
from testapp.models import Company
# Create your views here.
class Companylist(ListView):
    model=Company

class CompanyDetail(DetailView):
    model=Company   

class CompanyCreate(CreateView):
    model=Company
    fields="__all__"
    