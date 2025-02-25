from django.contrib import admin

from contacts.models import Contact


class ContactAdmin(admin.ModelAdmin):
    readonly_fields = ("pub_id",)
    fields = (
        "pub_id",
        "fn",
    )


admin.site.register(Contact, ContactAdmin)
