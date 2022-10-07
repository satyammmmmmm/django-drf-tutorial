import re
from django.shortcuts import render

# Create your views here.
def pagecount(request): 
    count=request.session.get('count',0)
    count+=1 
    request.session.set_expiry(10)
    request.session['count']=count
    print(request.session.get_expiry_age())

    return render(request,'testapp/pagecount.html',{'count':count})