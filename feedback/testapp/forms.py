
from django import forms 
from django.core import validators

class FeedBackForm(forms.Form):
    name=forms.CharField()
    rollno=forms.IntegerField()
    email=forms.EmailField()
    feedback=forms.CharField(widget=forms.Textarea)
   
    def clean(self):
        print("total for,")
        total_cleaned_data=super().clean()
        print("name validate")
        name=total_cleaned_data['name']
        if name[0].lower()!='d':
            forms.ValidationError("name")