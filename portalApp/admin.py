from django.contrib import admin

from portalApp.models import RecruiterProfile, ApplicantProfile, job_model

# Register your models here.
admin.site.register(RecruiterProfile)
admin.site.register(ApplicantProfile)
admin.site.register(job_model)