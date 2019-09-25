from django.contrib import admin
from jobapp.models import HydJob
from jobapp.models import PuneJob
from jobapp.models import BangaloreJob
from jobapp.models import ChennaiJob

# Register your models here.


class JobAdmin(admin.ModelAdmin):
    list_display = ['posting_date','job_title','location','position','eligibility','last_date','more_information']


admin.site.register(HydJob, JobAdmin)
admin.site.register(PuneJob, JobAdmin)
admin.site.register(BangaloreJob, JobAdmin)
admin.site.register(ChennaiJob, JobAdmin)
