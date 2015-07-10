from django.db import models
from django.core.validators import RegexValidator

class Contact(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be in the format: '+####', with 15 digits MAX.")

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(validators=[phone_regex], max_length=20, blank=True)

class Message(models.Model):
    sender = models.ForeignKey(Contact)
    content = models.CharField(max_length=160)
    received_at = models.DateTimeField(auto_now_add=True)
