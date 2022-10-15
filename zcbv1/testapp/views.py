from django.shortcuts import render
from django.views.generic import View
from django.views.generic import TemplateView
from django.http import HttpResponse
# Create your views here.
class HelloWorld(View):
    def get(self,request):
        return HttpResponse('<h1>from class based view</h1>')

# Create your views here.
class TemplateCBV(TemplateView):
    template_name='testapp/results.html'

class TemplateCBV2(TemplateView):
    template_name='testapp/results2.html'
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['name']='sat'
        return context