from django.contrib import admin
from testapp.models import HydJobs,BangloreJobs,PuneJobs

# Register your models here.
class HydJobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','email','address']
admin.site.register(HydJobs,HydJobsAdmin)

class BangloreJobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','email','address']
admin.site.register(BangloreJobs,BangloreJobsAdmin)

class PuneJobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','email','address']
admin.site.register(PuneJobs,PuneJobsAdmin)