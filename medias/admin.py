from django.contrib import admin
from . import models


@admin.register(models.MachineAndEquipment)
class MachineAndEquipmentAdmin(admin.ModelAdmin):
    list_display = ["name"]
