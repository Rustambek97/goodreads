from django.urls import path

from books.views import HomeView, BookListView, BookDetailView, BookReviewView

urlpatterns = [
    path('', HomeView, name='home'),
    path('books/', BookListView.as_view(), name='booklist'),
    path('books/<a>/', BookDetailView.as_view(), name='bookdetail'),
    path('<b>/review/', BookReviewView.as_view(), name='bookreview')
]

