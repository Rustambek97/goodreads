from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from django.views import View

class RegistrView(View):
    def get(self, request):
        return render(request, "users/registratsiya.html")

    def post(self, request):
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )
        user.save()
        return redirect("login")

class LoginView(View):
    def get(self, request):
        return render(request, "users/login.html")
