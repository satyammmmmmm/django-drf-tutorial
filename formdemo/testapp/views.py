from django.shortcuts import render
from testapp.forms import StudentForm
# Create your views here.
def student_input_view(request):
    submitted=False
    form=StudentForm()
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            print(form.cleaned_data['marks'])
            submitted=True
        form=StudentForm()    
    return render(request,'testapp/input.html',{'form':form},{'submitted':submitted})