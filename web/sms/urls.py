from django.conf.urls import url
from .views import *

urlpatterns = [
        url(r'^/$', MessageView.as_view(), name="sms"),
]
