from django.shortcuts import render
import datetime
# Create your views here.
def result(request):
    date = datetime.datetime.now()
   
    name = 'django'
    prerequisite  = 'python'
    mydict ={'msg':date,'name':name,'prerequisite':prerequisite}
    return render(request,'testapp/results.html',context=mydict)