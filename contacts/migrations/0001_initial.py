# Generated by Django 5.1.6 on 2025-02-06 07:24

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="created"),
                ),
                (
                    "modified",
                    models.DateTimeField(auto_now=True, verbose_name="modified"),
                ),
                (
                    "full_name",
                    models.CharField(
                        help_text="Full Name as written naturally. Max 100 char.",
                        max_length=100,
                        verbose_name="Full Name",
                    ),
                ),
                (
                    "non_latin_full_name",
                    models.CharField(
                        blank=True,
                        help_text="Full Name in non latin characters. Blank is ok. Max 100 char.",
                        max_length=100,
                        verbose_name="Non Latin Name",
                    ),
                ),
                (
                    "x_handle",
                    models.CharField(
                        blank=True,
                        help_text="Blank is ok. Max 100 char.",
                        max_length=100,
                        verbose_name="X Handle",
                    ),
                ),
                (
                    "avatar_url",
                    models.URLField(
                        blank=True,
                        help_text="Blank is ok. Max 255 char.",
                        max_length=255,
                        verbose_name="Avatar URL",
                    ),
                ),
                (
                    "notes",
                    models.TextField(
                        blank=True, help_text="Blank is ok.", verbose_name="Notes"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
