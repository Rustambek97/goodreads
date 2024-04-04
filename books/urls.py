from django.urls import path

from books.views import BookListView, BookDetailView, BookReviewView, BookEditView, BookDeleteView

urlpatterns = [
    path('books/', BookListView.as_view(), name='booklist'),
    path('books/<a>/', BookDetailView.as_view(), name='bookdetail'),
    path('<b>/review/', BookReviewView.as_view(), name='bookreview'),
    path('edit/<id>', BookEditView.as_view(), name="bookedit"),
    path('delete/<id>', BookDeleteView.as_view(), name='bookdelete')
]

