from django.contrib.auth import get_user
from django.test import TestCase
from django.urls import reverse

from users.models import CustomUser

class RegisterTestCase(TestCase):
    def test_register_successfull(self):
        self.client.post(
            reverse("register"),
            data={
                "username":"Testlovchi",
                "first_name":"Rustambek",
                "last_name":"Baltayev",
                "email":"r.baltayev9997@gmail.com",
                "password":"somepassword"
            }
        )

        user_count = CustomUser.objects.all().count()
        user = CustomUser.objects.get(username="Testlovchi")

        self.assertEqual(user_count, 1)
        self.assertEqual(user.username, "Testlovchi")
        self.assertEqual(user.first_name, "Rustambek")
        self.assertEqual(user.last_name, "Baltayev")
        self.assertEqual(user.email, "r.baltayev9997@gmail.com")
        self.assertNotEqual(user.password, "somepassword")
        self.assertTrue(user.check_password("somepassword"))

    def test_register_invalid(self):
        response = self.client.post(
            reverse("register"),
            data={
                "first_name": "Rustambek",
                "last_name": "Baltayev",
                "email": "r.baltayev9997@gmail.com",
            }
        )

        user_count = CustomUser.objects.all().count()

        self.assertEqual(user_count, 0)
        self.assertFormError(response, "form", "username", "This field is required.")
        self.assertFormError(response, "form", "password", "This field is required.")

    def test_enter_email_valid(self):
        response = self.client.post(
            reverse("register"),
            data={
                "username":"Testlovchi",
                "first_name": "Rustambek",
                "last_name": "Baltayev",
                "email": "r.baltayev9997",
                "password":"somepassword"
            }
        )

        user_count = CustomUser.objects.all().count()
        self.assertEqual(user_count, 0)
        self.assertFormError(response, "form", "email", "Enter a valid email address.")

class LoginTestCase(TestCase):
    def test_login_successfull(self):
        user = CustomUser.objects.create_user(
            username="Testlovchi",
            first_name="Rustambek",
            last_name="Baltayev",
            email="r.baltayev9997@gmail.com",
            password="somepassword"
        )
        user.save()
        response = self.client.post(
            reverse("login"),
            data={
                "username":"Testlovchi",
                "password":"somepassword"
            }
        )

        user = get_user(self.client)
        self.assertTrue(user.is_authenticated)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse("home"))



