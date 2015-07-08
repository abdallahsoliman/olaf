from django.test import TestCase, Client
from authenticate.factories import UserFactory
from django.contrib.auth import authenticate
from models import User

class UserTestCase(TestCase):
    def setUp(self):
        #self.user = UserFactory.create()
        self.user = User.objects.create(first_name="bob", last_name="bill", password="password123", email="bill@example.com")

    def test_can_create_user(self):
        self.assertIsNotNone(self.user.first_name)
        self.assertIsNotNone(self.user.last_name)
        self.assertIsNotNone(self.user.email)
        self.assertIsNotNone(self.user.password)

    def test_can_authenticate_user(self):
    	client = Client()
    	print User.objects.get(email=self.user.email).password
    	print authenticate(email=self.user.email, password='password123')
        print client.login(email=self.user.email, password='password123')
