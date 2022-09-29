from django.shortcuts import render
import datetime

# Create your views here.
def dateview(request):
    date=datetime.datetime.now()
    mydict={'msg':date}
    return render(request,'tempapp1/date.html',context=mydict)

    