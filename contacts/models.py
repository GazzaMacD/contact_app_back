from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import TimeStampedModel


class Contact(TimeStampedModel):
    """
    Base Model for contacts to be stored in
    """

    name = models.CharField(
        _("Name"),
        null=False,
        blank=False,
        max_length=100,
    )
    non_latin_name = models.CharField(
        _("Non Latin Name"),
        null=False,
        blank=True,
        max_length=100,
    )
    x_handle = models.CharField(
        _("X Handle"),
        null=False,
        blank=True,
        max_length=100,
    )
    avatar_url = models.URLField(
        _("Avatar URL"),
        null=False,
        blank=True,
        max_length=255,
    )
    notes = models.TextField(
        _("Notes"),
        null=False,
        blank=True,
    )

    def __str__(self) -> str:
        return self.name
