from django.db import models
class Custommanager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(esal__gte=5297)
class Custommanager2(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(esal__lte=5297)
# Create your models here.
class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=30)
    esal=models.IntegerField()
    eaddr=models.CharField(max_length=322)
    objects=Custommanager()
class proxyEmployee(Employee):
    objects=Custommanager2()

    class Meta:
        proxy=True