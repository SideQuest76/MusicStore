from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User

class AuthTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='pass123')

    def test_login_success(self):
        response = self.client.post('/api/auth/login/', {'username': 'testuser', 'password': 'pass123'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('token', response.data)

    def test_register(self):
        response = self.client.post('/api/auth/register/', {
            'username': 'newuser', 'password': 'newpass123', 'email': 'new@user.com'
        })
        self.assertEqual(response.status_code, 201)
