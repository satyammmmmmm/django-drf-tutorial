from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=30)
    rollno=models.IntegerField()
    dob=models.DateField()
    marks=models.IntegerField()
    email=models.EmailField()
    
    address=models.TextField()
    