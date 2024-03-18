from django.shortcuts import render, redirect
from django.views import View

from books.models import Book

def HomeView(request):
    return render(request, "home.html")

class BookListView(View):
    def get(self, request):
        kitoblar = Book.objects.all()
        return render(request, "books/booklist.html", {'kitoblar':kitoblar})


class BookDetailView(View):
    def get(self, request, a):
        kitob = Book.objects.get(id=a)
        return render(request, "books/bookdetail.html", {'kitob':kitob})


