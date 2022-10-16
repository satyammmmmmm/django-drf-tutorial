from django.http import HttpResponse


class appmaintain(object):
    def __init__(self,get_response):
        self.get_response=get_response 
    def __call__(self,request):
        response=self.get_response(request)
        return response

    def process_exception(self,request,exception):
        
        
        return HttpResponse(f'<h1>current some problem in app<br>error is :{exception.__class__.__name__}<br>exception is:{exception}</h1>')        



