from django.shortcuts import render
from testapp.models import Student
from testapp.forms import StudentForm

def student_view(request):
    form=StudentForm()
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            print("insert successfully")
# Create your views here.
    return render(request,'testapp/student.html',{'form':form})
