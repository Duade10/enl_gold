from django.db import models
from core.models import AbstractTimestamp
from django.utils.text import gettext_lazy as _


class Event(AbstractTimestamp):
    name = models.CharField(_("Event Name"), max_length=100)
    topic = models.CharField(_("Topic"), max_length=100, blank=True, null=True)
    by = models.CharField(_("By"), max_length=100, blank=True, null=True)
    to = models.CharField(_("To"), max_length=100, blank=True, null=True)
    description = models.TextField(_("Description"))
    picture = models.ImageField(_("Picture"), upload_to="event/main/")

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name


class EventImage(AbstractTimestamp):
    event = models.ForeignKey(Event, verbose_name=_("Event"), related_name="images", on_delete=models.CASCADE)
    file = models.ImageField(_("Event Image File"))

    def __str__(self):
        return f"{self.event.name} Image"

