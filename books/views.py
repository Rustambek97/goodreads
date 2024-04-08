from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from books.forms import BookReviewForm, BookEditForm
from books.models import Book, Review


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

class AdminCheck(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser


class BookEditView(LoginRequiredMixin,AdminCheck,View):
    def get(self, request, id):
        form = BookEditForm()
        return render(request, "books/bookedit.html", {"form":form})

    def post(self, request, id):
        form = BookEditForm(data=request.POST)

        if form.is_valid():
            kitob = Book.objects.filter(id=id)
            kitob.update(title=form.cleaned_data['title'],description=form.cleaned_data['description'])

            return redirect("booklist")

        return render(request, "books/bookedit.html", {"form":form})


class BookDeleteView(LoginRequiredMixin,AdminCheck,View):
    def get(self, request, id):
        kitob = Book.objects.get(id=id)
        kitob.delete()
        messages.success(request, "Siz kitob o'chirdingiz!")
        return redirect("booklist")


class DeleteReview(View):
    def get(self, request, id):
        review = Review.objects.get(id=id)
        kitobid = review.book_id.id
        review.delete()

        return redirect(reverse("bookdetail", kwargs={'a':kitobid}))

class EditReview(View):
    def get(self, request, sharxid):
        sharx = Review.objects.get(id=sharxid)
        edit_form = BookEditForm(instance=sharx)
        return render(request, "books/editreview.html", {'form':edit_form, 'sharxid':sharxid})

    def post(self, request, sharxid):
        sharx = Review.objects.get(id=sharxid)
        edit_form = BookEditForm(data=request.POST, instance=sharx)
        kitobid = sharx.book_id.id

        if edit_form.is_valid():
            edit_form.save()
            return redirect(reverse("bookdetail", kwargs={'a':kitobid}))

        return render(request, "books/editreview.html", {'form': edit_form, 'sharxid': sharxid})