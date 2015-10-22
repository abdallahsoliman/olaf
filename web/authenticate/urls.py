from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

urlpatterns = [
        url('^login/$', auth_views.login, {'template_name': 'authenticate/login.html'}),
    ]
