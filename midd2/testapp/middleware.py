from django.http import HttpResponse


class appmaintain(object):
    def __init__(self,get_response):
        self.get_response=get_response 
    def __call__(self,request):
        return HttpResponse('<h1>under maintaianenece</h1>')

