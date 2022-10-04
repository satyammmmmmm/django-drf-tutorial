from django.shortcuts import render
from testapp.forms import FeedBackForm
# Create your views here.
def feedback_view(request):
    form=FeedBackForm()
    if request.method=="POST":
        form=FeedBackForm(request.POST)
        if form.is_valid():
            print("all is well")
            print(form.cleaned_data['email'])
            print(form.cleaned_data['rollno'])

        else:
            print("failed")
    form=FeedBackForm()
    return render(request,'testapp/feedback.html',{'form':form})
