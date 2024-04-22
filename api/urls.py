from django.urls import path

from api.views import BookReviewApi, BookReviewListApi

urlpatterns = [
    path("review/<id>/", BookReviewApi.as_view(), name='review-detail'),
    path("reviews/", BookReviewListApi.as_view(), name='reviews-list')
]
