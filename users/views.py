from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import UserRegistrForm, UserLoginForm
from django.views import View

class RegistrView(View):
    def get(self, request):
        user = UserRegistrForm()
        return render(request, "users/registratsiya.html", {'form':user})

    def post(self, request):
        user = UserRegistrForm(data=request.POST)
        if user.is_valid():
            user.save()
            return redirect("login")
        else:
            return render(request, "users/registratsiya.html", {'form': user})

class LoginView(View):
    def get(self, request):
        user = UserLoginForm()
        return render(request, "users/login.html", {'user':user})

    def post(self, request):
        check = AuthenticationForm(data=request.POST)

        if check.is_valid():
            user = check.get_user()
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("home")

