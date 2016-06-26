from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext, ugettext_lazy as _
from django import forms

class LoginForm(AuthenticationForm):
    username = forms.CharField(
                label="",
                max_length=254,
                widget=forms.TextInput(attrs={'placeholder': 'Email Address', 'autofocus': '', 'class': ''}),
            )
    password = forms.CharField(
                label="",
                widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': ''}),
            )
