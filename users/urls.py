from django.urls import path

from users.views import RegistrView, LoginView, LogoutView, ProfileView

urlpatterns = [
    path('register/', RegistrView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile')
]
