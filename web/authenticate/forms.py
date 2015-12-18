from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext, ugettext_lazy as _
from django import forms

class LoginForm(AuthenticationForm):

    username = forms.CharField(
            max_length=254,
            widget=forms.TextInput(attrs={'autofocus': '', 'class': 'mdl-textfield__input'}),
            )
    password = forms.CharField(
            label=_("Password"),
            widget=forms.PasswordInput(attrs={'class': 'mdl-textfield__input'})
            )
