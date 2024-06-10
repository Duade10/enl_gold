from django.db import models
from core.models import AbstractTimestamp
from django.utils.text import gettext_lazy as _


class MachineAndEquipment(AbstractTimestamp):
    name = models.CharField(_("Machine/Equipment Name"), max_length=100)
    description = models.TextField(_("Machine/Equipment Description"))
    picture = models.ImageField(_("Machine/Equipment Picture"), upload_to="machine/")

    class Meta:
        verbose_name = "Machine and Equipment"
        verbose_name_plural = "Machines and Equipments"

    def __str__(self):
        return self.name
