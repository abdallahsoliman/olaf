from django.conf.urls import url
from dorm.views import *

urlpatterns = [
        url(r'^/$', DormView.as_view(), name="dorm"),
        url(r'actuators/$', ActuatorView.as_view()),

]
