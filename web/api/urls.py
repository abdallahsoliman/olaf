from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from api import views

router = routers.SimpleRouter()

# authenticate
router.register(r'users', views.UserViewSet, base_name='user')
# sms
router.register(r'messages', views.MessageViewSet, base_name="message")
router.register(r'contacts', views.ContactViewSet, base_name="contact")

urlpatterns = [
    url(r'^auth/token/', obtain_auth_token),
]
urlpatterns += router.urls
