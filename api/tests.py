from django.urls import reverse
from rest_framework.test import APITestCase

# Create your tests here.
from books.models import Book, Review
from users.models import CustomUser


class BookReviewApiTestCase(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username="Testlovchi", password="123456789", first_name="Rustambek")
        self.client.login(username="Testlovchi", password="123456789")

    def test_book_review_detail(self):
        book = Book.objects.create(title="Book1", description="Description1", isbn="123123123")
        review = Review.objects.create(book_id=book, user_id=self.user, description="very good book", stars=5)

        response = self.client.get(reverse("review-detail", kwargs={"id":review.id}))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['id'], review.id)
        self.assertEqual(response.data['stars'], 5)
        self.assertEqual(response.data['description'], "very good book")
        self.assertEqual(response.data['user_id']['id'], self.user.id)
        self.assertEqual(response.data['user_id']['first_name'], self.user.first_name)
        self.assertEqual(response.data['user_id']['username'], self.user.username)
        self.assertEqual(response.data['book_id']['id'], book.id)
        self.assertEqual(response.data['book_id']['title'], "Book1")
        self.assertEqual(response.data['book_id']['description'], "Description1")

    def test_book_review_list(self):
        user2 = CustomUser.objects.create_user(username="Testlovchi2", password="123456789", first_name="Rustambek")

        book = Book.objects.create(title="Book1", description="Description1", isbn="123123123")
        review = Review.objects.create(book_id=book, user_id=self.user, description="very good book", stars=5)
        review2 = Review.objects.create(book_id=book, user_id=user2, description="not good", stars=1)

        response = self.client.get(reverse("reviews-list"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['results'][1]['id'], review2.id)
        self.assertEqual(response.data['results'][0]['id'], review.id)

        self.assertEqual(response.data['results'][1]['description'], "not good")
        self.assertEqual(response.data['results'][0]['description'], "very good book")

        self.assertEqual(response.data['results'][1]['stars'], 1)
        self.assertEqual(response.data['results'][0]['stars'], 5)

        self.assertEqual(response.data['results'][1]['book_id']['id'], book.id)
        self.assertEqual(response.data['results'][1]['book_id']['title'], book.title)
        self.assertEqual(response.data['results'][1]['book_id']['description'], book.description)
        self.assertEqual(response.data['results'][1]['book_id']['isbn'], book.isbn)

        self.assertEqual(response.data['results'][0]['book_id']['id'], book.id)
        self.assertEqual(response.data['results'][0]['book_id']['title'], book.title)
        self.assertEqual(response.data['results'][0]['book_id']['description'], book.description)
        self.assertEqual(response.data['results'][0]['book_id']['isbn'], book.isbn)

        self.assertEqual(response.data['results'][1]['user_id']['username'], user2.username)
        self.assertEqual(response.data['results'][1]['user_id']['first_name'], user2.first_name)

        self.assertEqual(response.data['results'][0]['user_id']['username'], self.user.username)
        self.assertEqual(response.data['results'][0]['user_id']['first_name'], self.user.first_name)

