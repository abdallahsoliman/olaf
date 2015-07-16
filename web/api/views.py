from rest_framework import viewsets, generics
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

