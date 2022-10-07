from django.shortcuts import render

# Create your views here.

def index1(request):
    return render(request,'testapp/index.html')

def movieview(request):
    headmsg="UP MOVIE NEWS"
    m1="OTT is result of covid"
    m2="30 sep ps-1 releases"
    mydict={'headmsg':headmsg,'m1':m1,'m2':m2}
    return render(request,'testapp/news.html',mydict)