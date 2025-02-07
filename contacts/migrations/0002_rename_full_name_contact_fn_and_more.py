# Generated by Django 5.1.6 on 2025-02-06 08:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("contacts", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="contact",
            old_name="full_name",
            new_name="fn",
        ),
        migrations.RemoveField(
            model_name="contact",
            name="non_latin_full_name",
        ),
        migrations.AddField(
            model_name="contact",
            name="non_latin_fn",
            field=models.CharField(
                blank=True,
                help_text="Full Name in non latin characters. Blank is ok. Max 100 char.",
                max_length=100,
                verbose_name="Non Latin Full Name",
            ),
        ),
    ]
