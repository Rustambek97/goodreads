from django.urls import path

from users.views import RegistrView, LoginView

urlpatterns = [
    path('register/', RegistrView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login')
]