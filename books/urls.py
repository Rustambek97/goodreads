from django.urls import path

from books.views import BookListView, \
    BookDetailView, \
    BookReviewView, \
    BookEditView, \
    BookDeleteView, \
    DeleteReview, \
    EditReview

urlpatterns = [
    path('books/', BookListView.as_view(), name='booklist'),
    path('books/<a>/', BookDetailView.as_view(), name='bookdetail'),
    path('<b>/review/', BookReviewView.as_view(), name='bookreview'),
    path('edit/<id>', BookEditView.as_view(), name="bookedit"),
    path('delete/<id>', BookDeleteView.as_view(), name='bookdelete'),
    path('reviewdelete/<id>', DeleteReview.as_view(), name='reviewdelete'),
    path('reviewedit/<sharxid>', EditReview.as_view(), name='reviewedit'),

]

