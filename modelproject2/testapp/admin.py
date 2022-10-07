from django.contrib import admin
from testapp.models import student
# Register your models here.
class studentAdmin(admin.ModelAdmin):
    list_display = ['id','name','marks']


admin.site.register(student,studentAdmin)
