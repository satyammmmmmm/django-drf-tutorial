from django.shortcuts import render
from testapp.forms import StudentForm
# Create your views here.
def student_input_view(request):
    form=StudentForm()
    return render(request,'testapp/input.html',{'form':form})