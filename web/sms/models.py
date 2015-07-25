from django.db import models
from django.core.validators import RegexValidator
from authenticate.models import User

class Contact(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=100)

    @classmethod
    def exists(cls, name, number):
        contact = cls.objects.filter(name=name).first()
        return (contact is not None)

    def has_number(self, number):
        number = self.phonenumber_set.filter(number=number).first()
        return (number is not None)

    @classmethod
    def create_or_add_number(cls, user, name, number):
        contact = cls.objects.filter(name=name).first()
        if (contact is not None and not contact.has_number(number)):
            number = PhoneNumber.objects.create(contact=contact, number=number)
        elif (contact is None):
            contact = Contact.objects.create(user=user, name=name)
            PhoneNumber.objects.create(contact=contact, number=number)

        return contact


class PhoneNumber(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be in the format: '+####', with 15 digits MAX.")

    contact = models.ForeignKey(Contact)
    number = models.CharField(validators=[phone_regex], max_length=20, blank=True)

    class Meta:
        unique_together = ("contact", "number")

class Message(models.Model):
    sender = models.ForeignKey(Contact)
    user = models.ForeignKey(User)
    content = models.CharField(max_length=160)
    received_at = models.DateTimeField(auto_now_add=True)
