from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import TimeStampedModel


class Contact(TimeStampedModel):
    """
    Base Model for contacts to be stored in
    """

    fn = models.CharField(
        _("Full Name"),
        null=False,
        blank=False,
        max_length=100,
        help_text=_("Full Name as written naturally. Max 100 char."),
    )
    non_latin_fn = models.CharField(
        _("Non Latin Full Name"),
        null=False,
        blank=True,
        max_length=100,
        help_text=_("Full Name in non latin characters. Blank is ok. Max 100 char."),
    )
    favorite = models.BooleanField(
        _("Favorite"),
        null=False,
        blank=False,
    )
    x_handle = models.CharField(
        _("X Handle"),
        null=False,
        blank=True,
        max_length=100,
        help_text=_("Blank is ok. Max 100 char."),
    )
    avatar_url = models.URLField(
        _("Avatar URL"),
        null=False,
        blank=True,
        max_length=255,
        help_text=_("Blank is ok. Max 255 char."),
    )
    notes = models.TextField(
        _("Notes"), null=False, blank=True, help_text=_("Blank is ok.")
    )

    def __str__(self) -> str:
        return self.fn
