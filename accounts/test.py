from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class AccountsTests(TestCase):
    def setUp(self):
        self.username = 'testuser'
        self.password = 'password123'
        self.user = User.objects.create_user(username=self.username, password=self.password)
        
    def test_signup_page_status_code(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_signup_form(self):
        response = self.client.post(reverse('signup'), {
            'username': 'newuser',
            'password1': 'Password123!',
            'password2': 'Password123!',
        })
        self.assertEqual(response.status_code, 302)  # Redirects after successful signup
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_signup_form_invalid(self):
        response = self.client.post(reverse('signup'), {
            'username': 'newuser',
            'password1': 'password',
            'password2': 'password',
        })
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'password1', '비밀번호는 최소 8자 이상이어야 합니다.')

    def test_login_page_status_code(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_login_form(self):
        response = self.client.post(reverse('login'), {
            'username': self.username,
            'password': self.password,
        })
        self.assertEqual(response.status_code, 302)  # Redirects after successful login

    def test_login_form_invalid(self):
        response = self.client.post(reverse('login'), {
            'username': self.username,
            'password': 'wrongpassword',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '사용자 이름 또는 비밀번호가 올바르지 않습니다.')