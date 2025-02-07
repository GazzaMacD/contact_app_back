from rest_framework import serializers
from .models import Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = [
            "id",
            "fn",
            "non_latin_fn",
            "favorite",
            "x_handle",
            "avatar_url",
            "notes",
        ]
