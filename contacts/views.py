from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from contacts.models import Contact
from contacts.serializers import ContactSerializer


class ContactList(APIView):
    """
    List all contacts or create new contact
    """

    def get(self, request, format=None):
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)


class ContactDetail(APIView):
    """
    Get, update or delete a contact
    """

    def get_object(self, pub_id):
        try:
            return Contact.objects.get(pub_id=pub_id)
        except Contact.DoesNotExist:
            raise Http404

    def get(self, request, pub_id, format=None):
        snippet = self.get_object(pub_id)
        serializer = ContactSerializer(snippet)
        return Response(serializer.data)
