import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','studentinfo.settings')

import django
django.setup()

from faker import Faker 
from testapp.models import student

fake=Faker()
frollno=fake.random_int(min=1,max=999)
fname=fake.name()
fdob=fake.date()
fmarks=fake.random_int(min=1,max=100)
femail=fake.email()
faddress=fake.address()
fp=99999

student_record=student.objects.get_or_create(name=fname,rollno=frollno,dob=fdob,phonenumber=fp,marks=fmarks,email=femail,address=faddress)




