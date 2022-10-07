from django.contrib import admin
from testapp.models import emp
# Register your models here.
class empAdmin(admin.ModelAdmin):
    list_display=['eno','ename','esal','eaddr']

admin.site.register(emp,empAdmin)
