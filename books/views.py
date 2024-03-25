from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views import View

from books.models import Book

def HomeView(request):
    return render(request, "home.html")

class BookListView(View):
    def get(self, request):
        kitoblar = Book.objects.all().order_by('id')
        search_query = request.GET.get('q', '')
        kitoblar = kitoblar.filter(title__icontains=search_query)

        paginator = Paginator(kitoblar, 2)

        page_num = request.GET.get('bet', 1)
        page = paginator.page(page_num)
        if search_query:
            return render(request, "books/booklist.html", {'page':page, 'search':search_query})
        return render(request, "books/booklist.html", {'page':page})


class BookDetailView(View):
    def get(self, request, a):
        kitob = Book.objects.get(id=a)
        return render(request, "books/bookdetail.html", {'kitob':kitob})


