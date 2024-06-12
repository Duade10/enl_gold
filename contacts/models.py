from django.db import models
from django.utils.text import gettext_lazy as _

from core.models import AbstractTimestamp


class ContactMessage(AbstractTimestamp):
    name = models.CharField(_("Name"), max_length=100)
    email = models.EmailField(_("Email"))
    subject = models.CharField(_("Subject"), max_length=200)
    message = models.TextField(_("Message"))

    def __str__(self):
        return f"{self.name}  - {self.email}"
