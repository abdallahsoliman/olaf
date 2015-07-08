from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.core.validators import RegexValidator


class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password):
        if not email:
            raise ValueError("Users must have a valid email.")
        if not first_name:
            raise ValueError("User must have a valid first name.")
        if not last_name:
            raise ValueError("User must have a valid last name.")
        if not password:
            raise ValueError("User must have a valid password.")

        user = self.model(email=self.normalize_email(email), first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be in the format: '+####', with 15 digits MAX.")
    password_regex = RegexValidator(regex=r'((?=.*\d)(?=.*[a-z]).{6,20})',
                                    message="Password must be alphanumeric and between 6 and 20 characters.")

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(validators=[phone_regex], max_length=20, blank=True)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_short_name(self):
            return self.first_name

    def get_full_name(self):
        return "%s %s" % (self.first_name, self.last_name)

    def __unicode__(self):
        return self.email
