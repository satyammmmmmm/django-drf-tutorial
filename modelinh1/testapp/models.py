from django.db import models

# Create your models here.
class ContactInfo(models.Model):
    name=models.CharField(max_length=64)
    email=models.EmailField()
    address=models.CharField(max_length=64)
    class Meta:
        abstract=True 
class Student(ContactInfo):
    rollno=models.IntegerField()
    marks=models.IntegerField()

class Teacher(ContactInfo):
    subject=models.CharField(max_length=64)
    salary=models.FloatField()

class ContactInfo1(models.Model):
    name=models.CharField(max_length=64)
    email=models.EmailField()
    address=models.CharField(max_length=64)
class Student1(ContactInfo):
    rollno=models.IntegerField()
    marks=models.IntegerField()

class Teacher1(ContactInfo):
    subject=models.CharField(max_length=64)
    salary=models.FloatField()

class Person(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()

class Employee(Person):
    eno=models.IntegerField()
    esal=models.IntegerField()

class Manager(Employee):
    exp=models.IntegerField()
    teamsize=models.IntegerField()


class parent1(models.Model):
    f1=models.CharField(max_length=54)
    f1=models.CharField(max_length=54)

class parent2(models.Model):
    f3=models.CharField(max_length=54,primary_key=True)
    f4=models.CharField(max_length=54)

class child(parent1,parent2):
     f5=models.CharField(max_length=54)
     f6=models.CharField(max_length=54)

