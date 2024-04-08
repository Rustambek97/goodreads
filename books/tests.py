from django.test import TestCase

# Create your tests here.
from django.urls import reverse

from books.models import Book


class BookTestCase(TestCase):
    def test_book_list(self):
        Book.objects.create(title="new book1", description="report1", isbn="123456789")
        Book.objects.create(title="new book2", description="report2", isbn="123456789")

        response = self.client.get(reverse("booklist"))

        kitob1 = Book.objects.get(title="new book1")
        kitob2 = Book.objects.get(title="new book2")

        self.assertContains(response, kitob1.title)
        self.assertContains(response, kitob2.title)

    def test_search_books(self):
        Book.objects.create(title="new book1", description="report1", isbn="123456789")
        Book.objects.create(title="new book2", description="report2", isbn="123456789")
        Book.objects.create(title="new book3", description="report3", isbn="123456789")
        Book.objects.create(title="new book4", description="report4", isbn="123456789")

        response = self.client.get(reverse("booklist")+"?q=book1")

        kitob1 = Book.objects.get(title="new book1")
        kitob2 = Book.objects.get(title="new book2")

        self.assertContains(response, kitob1.title)
        self.assertNotContains(response, kitob2.title)

    def test_not_books(self):
        response = self.client.get(reverse("booklist"))

        self.assertContains(response, "Kitoblar topilmadi")

    def test_search_not_books(self):
        Book.objects.create(title="new book1", description="report1", isbn="123456789")
        Book.objects.create(title="new book2", description="report2", isbn="123456789")
        Book.objects.create(title="new book3", description="report3", isbn="123456789")
        Book.objects.create(title="new book4", description="report4", isbn="123456789")

        response = self.client.get(reverse("booklist") + "?q=book12")

        self.assertContains(response, "Kitoblar topilmadi")