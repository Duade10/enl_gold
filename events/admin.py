from django.contrib import admin
from . import models


class EventImageInline(admin.TabularInline):
    model = models.EventImage


@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ["name", "topic", "by", "to"]
    inlines = [EventImageInline,]
