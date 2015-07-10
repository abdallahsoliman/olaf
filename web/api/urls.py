from django.conf.urls import url, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()

# authenticate
router.register(r'users', views.UserViewSet)
# sms
router.register(r'messages', views.MessageViewSet)
router.register(r'contacts', views.ContactViewSet)

urlpatterns = []
urlpatterns += router.urls
