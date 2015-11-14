from django.conf.urls import url
from health.views import *

urlpatterns = [
        url(r'^/$', HeartRateView.as_view(), name='health'),
        url(r'heart-rate/$', HeartRateView.as_view()),
]
