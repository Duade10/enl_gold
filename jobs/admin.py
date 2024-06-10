from django.contrib import admin

from . import models


@admin.register(models.Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ["title", "location", "job_type", ]


@admin.register(models.Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "has_higher_education"]
