from django.db import models

class CustomManager(models.Manager):
    def get_queryset(self):
        qs=super().get_queryset().order_by('eno')
        return qs
    def getempsal(self,minsal,maxsal):
        qs=super().get_queryset().filter(esal__range=(minsal,maxsal))
        return qs
# Create your models here.
class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=30)
    esal=models.IntegerField()
    eaddr=models.CharField(max_length=322)
    objects=CustomManager()
# Create your models here.
