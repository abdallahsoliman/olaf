from django.conf import settings
from django.db.models import signals
from django.dispatch import receiver
from rest_framework.authtokens.models import Token

@receiver(signal.post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
