from django.db import models
from core.models import AbstractTimestamp
from django.utils.text import gettext_lazy as _


class TeamMember(AbstractTimestamp):
    full_name = models.CharField(_("Full Name"), max_length=100)
    position = models.CharField(_("Position"), max_length=100)
    facebook_url = models.URLField(_("Facebook URL"), blank=True, null=True)
    twitter_url = models.URLField(_("Twitter URL"), blank=True, null=True)
    linkedIn_url = models.URLField(_("LinkedIn URL"), blank=True, null=True)
    instagram_url = models.URLField(_("Instagram URL"), blank=True, null=True)
    profile_picture = models.ImageField(_("Profile Picture"), blank=True, null=True)

    def __str__(self):
        return self.full_name
