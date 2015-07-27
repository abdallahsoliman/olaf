from rest_framework import serializers
from authenticate.models import User
from sms.models import Contact, Message, PhoneNumber

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'password', 'email')

class ContactSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    phone_numbers = serializers.StringRelatedField(many=True)

    class Meta:
        model = Contact
        fields = ('user', 'name', 'phone_numbers')

class PhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneNumber
        fields = ('contact', 'number')

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('content', 'sender', 'received_at')
