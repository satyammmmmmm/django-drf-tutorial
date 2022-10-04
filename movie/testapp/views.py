from django.shortcuts import render
from testapp.models import Movie
from testapp.forms import MovieForm
# Create your views here.
def index_view(request):
    return render(request,'testapp/index.html')

def list_movies_view(request):
    movies_list=Movie.objects.all()
    return render(request,'testapp/listmovies.html',{'movies_list':movies_list})

def add_movie_view(request):
    form=MovieForm()
    
    form=MovieForm(request.POST)
    if request.method=="POST":
        form.save()
        return index_view(request)

    return render(request,'testapp/addmovie.html',{'form':form})