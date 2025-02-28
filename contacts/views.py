from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser

from contacts.models import Contact
from contacts.serializers import ContactSerializer


class ContactList(APIView):
    """
    List all contacts or create new contact
    """

    parser_classes = (JSONParser, MultiPartParser, FormParser)

    def get(self, request, format=None):
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
        contact = self.get_object(pub_id)
        serializer = ContactSerializer(contact)
        return Response(serializer.data)

    def patch(self, request, pub_id, format=None):
        contact = self.get_object(pub_id)
        serializer = ContactSerializer(contact, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pub_id, format=None):
        contact = self.get_object(pub_id)
        contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
