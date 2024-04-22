from django.http import JsonResponse
from django.views import View
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializer import ReviewSerializer
from books.models import Review

class BookReviewApi(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        review = Review.objects.get(id=id)
        serializer = ReviewSerializer(review)
        return Response(data=serializer.data)

    def delete(self, request, id):
        review = Review.objects.get(id=id)
        review.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id):
        review = Review.objects.get(id=id)
        serializer = ReviewSerializer(data=request.data, instance=review)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        review = Review.objects.get(id=id)
        serializer = ReviewSerializer(data=request.data, instance=review, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class BookReviewListApi(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        reviews = Review.objects.all()

        paginator = PageNumberPagination()
        page_obj = paginator.paginate_queryset(reviews, request)

        serializer = ReviewSerializer(page_obj, many=True)

        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = ReviewSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

