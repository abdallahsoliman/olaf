from django.test import TestCase
from authenticate.factories import UserFactory
from django.contrib.auth import authenticate
from models import User

class UserTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory.create()

    def test_can_create_user(self):
        self.assertIsNotNone(self.user.first_name)
        self.assertIsNotNone(self.user.last_name)
        self.assertIsNotNone(self.user.email)
        self.assertIsNotNone(self.user.password)

    def test_can_authenticate_user(self):
        self.assertEqual(authenticate(email=self.user.email, password='password123').email, self.user.email)
