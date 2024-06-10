from django.contrib import admin
from . import models


@admin.register(models.MachineAndEquipment)
class MachineAndEquipmentAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(models.PhotoAlbum)
class PhotoAlbumAdmin(admin.ModelAdmin):
    list_display = ["short_description"]