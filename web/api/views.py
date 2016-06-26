from rest_framework import viewsets, generics
from rest_framework.response import Response
from django.core.exceptions import ValidationError
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotModified
from authenticate.models import User
from message.models import Message, Contact
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
        try:
            contact = Contact.create_or_add_number(self.request.user, request.POST["name"], request.POST["number"])
            return Response(serializers.ContactSerializer(contact).data, status=201)
        except ValidationError as ex:
            if "__all__" in ex.message_dict:
                return HttpResponseNotModified()
            else:
                return HttpResponseBadRequest("%s is not a valid number" % request.POST["number"])
