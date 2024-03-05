from django.urls import path

from books.views import HomeView

urlpatterns = [
    path('', HomeView)
]