from django.contrib import admin

# Register your models here.

from testapp.models import Employee,proxyEmployee


class EmployeeAdmin(admin.ModelAdmin):
    ist_display=['eno','ename','esal','eaddr']
# Register your models here.
class proxyAdmin(admin.ModelAdmin):
    ist_display=['eno','ename','esal','eaddr']
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(proxyEmployee,proxyAdmin)