from django.db import models
from django.utils.text import gettext_lazy as _

from core.models import AbstractTimestamp


class Job(AbstractTimestamp):
    class JobType(models.TextChoices):
        FULL_TIME = "FT", _("Full-Time")
        PART_TIME = "PT", _("Part-Time")
        CONTRACT = "CT", _("Contract")
        INTERNSHIP = "IN", _("Internship")
        FREELANCE = "FL", _("Freelance")

    title: str = models.CharField(
        _("Job Title"),
        max_length=100,
    )
    location: str = models.CharField(
        _("Job Location"),
        max_length=100,
        blank=True,
    )
    job_type: str = models.CharField(
        _("Job Type"),
        max_length=2,
        choices=JobType.choices,
        default=JobType.FULL_TIME,
    )
    description: str = models.TextField(_("Job Description"))

    is_active: bool = models.BooleanField(_("Is Job Active"), default=True)

    class Meta:
        verbose_name = _("Job")
        verbose_name_plural = _("Jobs")
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.title} ({self.job_type}) - {self.location}"

    @property
    def is_remote(self):
        return self.location.lower() == "remote"


class Application(AbstractTimestamp):
    """The model for Job Applications """

    class GenderType(models.TextChoices):
        MALE = "M", _("Male")
        FEMALE = "F", _("Female")
        OTHER = "O", _("Other")

    class EducationLevel(models.TextChoices):
        NO_FORMAL_EDUCATION = "NFE", _("No formal education")
        PRIMARY = "PRI", _("Primary education")
        SECONDARY = "SEC", _("Secondary education")
        VOCATIONAL = "VOC", _("Vocational training")
        BACHELORS = "BAC", _("Bachelor's degree")
        MASTERS = "MAS", _("Master's degree")
        DOCTORATE = "PHD", _("Doctorate or higher")

    first_name = models.CharField(_("First Name"), max_length=50)
    last_name = models.CharField(_("Last Name"), max_length=50)
    date_of_birth = models.DateField(_("Date Of Birth"))
    gender = models.CharField(
        _("Gender"),
        max_length=1,
        choices=GenderType.choices
    )
    email = models.EmailField(_("Email"))
    phone_number = models.CharField(_("Phone Number"), max_length=20)
    address = models.TextField(_("Address"))
    highest_education_level = models.CharField(
        _("Highest Level of Education"),
        max_length=3,
        choices=EducationLevel.choices
    )
    school = models.CharField(_("School/University"), max_length=100)
    work_experience = models.TextField(_("Work Experience"))
    resume = models.FileField(_("Resume"), upload_to="resume/", blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}'s Profile"

    @property
    def has_higher_education(self):
        return self.highest_education_level in [
            self.EducationLevel.BACHELORS,
            self.EducationLevel.MASTERS,
            self.EducationLevel.DOCTORATE
        ]
