from rest_framework import serializers

# class UserSerializer(serializers.Serializer):
#     first_name = serializers.CharField(max_length=200)
#     last_name = serializers.CharField(max_length=200)
#     username = serializers.CharField(max_length=200)
#     email = serializers.EmailField(max_length=255)
#
# class BookSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=200)
#     description = serializers.CharField()
#     isbn = serializers.CharField(max_length=17)
#
# class BookReviewSerializer(serializers.Serializer):
#     stars = serializers.IntegerField(min_value=1, max_value=5)
#     description = serializers.CharField()
#     book_id = BookSerializer()
#     user_id = UserSerializer()
from books.models import Book, Review
from users.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'first_name', 'last_name', 'username', 'email')


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'description', 'isbn')


class ReviewSerializer(serializers.ModelSerializer):
    user_id = UserSerializer(read_only=True)
    book_id = BookSerializer(read_only=True)
    user_id_id = serializers.IntegerField(write_only=True)
    book_id_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Review
        fields = ('id', 'description','stars', 'user_id', 'book_id', 'user_id_id', 'book_id_id')
