from django.contrib import admin

from . import models


@admin.register(models.ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ["name", "email"]
