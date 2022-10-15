
from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from testapp.models import Book
# Create your views here.
class Booklist(ListView):
    model=Book
    template_name='testapp/books.html'
    context_object_name='books'
class BookDetail(DetailView):
    model=Book 

class BookCreateView(CreateView):
    model=Book
    fields=('title','author','pages')

class BookUpdateView(UpdateView): 
    model=Book 
    fields='__all__'  


#default templatefile=book_detail.html 
#default context=book or object
