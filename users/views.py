from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import UserRegistrForm, UserLoginForm, EditProfileForm
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
            messages.success(request, "Siz tizimga kirdingiz!")
            return redirect('home')
        else:
            return redirect('login')

class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.info(request, "Siz tizimdan chiqdingiz!")
        return redirect("home")

class ProfileView(LoginRequiredMixin,View):
    def get(self, request):
        return render(request, "users/profile.html")

class EditProfileView(LoginRequiredMixin, View):
    def get(self, request):
        form = EditProfileForm(instance=request.user)
        return render(request, "users/edit_profile.html", {'form':form})

    def post(self, request):
        form = EditProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Siz ma'lumotlaringizni muvofaqqiyatli o'zgartirdingiz!")
            return redirect('profile')
        return render(request, "users/edit_profile.html", {'form':form})