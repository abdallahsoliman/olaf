from rest_framework import viewsets, generics
from django.http import HttpResponse
from authenticate.models import User
from sms.models import Message, Contact
from api import serializers

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer

    def get_queryset(self):
        return [self.request.user]


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.MessageSerializer

    def get_queryset(self):
        return Message.objects.filter(user=self.request.user)

class ContactViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ContactSerializer

    def get_queryset(self):
        return Contact.objects.filter(user=self.request.user)

    def create(self, request):
        contact = Contact.create_or_add_number(self.request.user, request.POST["name"], request.POST["number"])
        return contact
