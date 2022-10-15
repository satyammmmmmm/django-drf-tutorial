from msilib.schema import ListView
from django.shortcuts import render
from django.views.generic import ListView
from testapp.models import Book
# Create your views here.
class Booklist(ListView):
    model=Book
    template_name='testapp/books.html'
