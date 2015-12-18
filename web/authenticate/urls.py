from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from .forms import LoginForm

urlpatterns = [
        url('^login/$', auth_views.login, {'authentication_form': LoginForm, 'template_name': 'authenticate/login.html'}, name="login"),
    ]
