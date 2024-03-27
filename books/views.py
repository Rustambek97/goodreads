from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from books.forms import BookReviewForm
from books.models import Book, Review


def HomeView(request):
    return render(request, "home.html")

class BookListView(View):
    def get(self, request):
        kitoblar = Book.objects.all().order_by('id')
        search_query = request.GET.get('q', '')
        if search_query:
            kitoblar = Book.objects.filter(title__icontains=search_query)

        paginator = Paginator(kitoblar, 2)

        page_num = request.GET.get('bet', 1)

        page = paginator.page(page_num)

        return render(request, "books/booklist.html", {'page':page, 'search':search_query})


class BookDetailView(View):
    def get(self, request, a):
        kitob = Book.objects.get(id=a)
        sharxlar = kitob.review_set.all()
        review_form = BookReviewForm()
        return render(request, "books/bookdetail.html", {'kitob':kitob, 'sharxlar':sharxlar, 'form':review_form})

class BookReviewView(LoginRequiredMixin,View):
    def post(self, request, b):
        review_form = BookReviewForm(data=request.POST)
        kitob = Book.objects.get(id=b)
        sharxlar = kitob.review_set.all()
        if review_form.is_valid():
            Review.objects.create(
                user_id=request.user,
                book_id=kitob,
                description=review_form.cleaned_data['description'],
                stars = review_form.cleaned_data['stars']
            )
            return redirect(reverse("bookdetail", kwargs={'a':kitob.id}))

        return render(request, "books/bookdetail.html", {'kitob':kitob, 'sharxlar':sharxlar, 'form':review_form})
