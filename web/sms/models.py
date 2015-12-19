import re
from django.core.validators import RegexValidator
from django.db import models
from authenticate.models import User

class Contact(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=100)

    @classmethod
    def exists(cls, name, number):
        contact = cls.objects.filter(name=name).first()
        return (contact is not None)

    def has_number(self, number):
        number = PhoneNumber.format_number(number)
        number = self.phone_numbers.filter(number=number).first()
        return (number is not None)

    @classmethod
    def create_or_add_number(cls, user, name, number):
        contact = cls.objects.filter(name=name).first()

        if (contact is None):
            contact = Contact.objects.create(user=user, name=name)

        phone_number = PhoneNumber(contact=contact, number=PhoneNumber.format_number(number))
        phone_number.full_clean()
        phone_number.save()

        return contact


class PhoneNumber(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be in the format: '+####', with 15 digits MAX.")

    contact = models.ForeignKey(Contact)
    number = models.CharField(validators=[phone_regex], max_length=20, blank=True)

    class Meta:
        default_related_name = "phone_numbers"
        unique_together = ("contact", "number")

    def __unicode__(self):
        return self.number

    @classmethod
    def format_number(cls, number):
        # TODO: improve regex
        number = "".join(re.findall('\d+', number))[:15]
        if len(number) == 9:
            number = "+1%s" % number
        else:
            number = "+%s" % number
        return number

class Message(models.Model):
    sender = models.ForeignKey(Contact)
    user = models.ForeignKey(User)
    content = models.CharField(max_length=1000)
    received_at = models.DateTimeField(auto_now_add=True)
