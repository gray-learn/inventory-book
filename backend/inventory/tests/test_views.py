from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from inventory.models import Book

class BookViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.book = Book.objects.create(
            title="Test Book",
            author="Test Author",
            genre="Test Genre",
            publication_date="2023-01-01",
            isbn="1234567890123"
        )

    def test_get_all_books(self):
        response = self.client.get(reverse('book-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_create_book(self):
        data = {
            "title": "New Book",
            "author": "New Author",
            "genre": "New Genre",
            "publication_date": "2023-02-02",
            "isbn": "9876543210987"
        }
        response = self.client.post(reverse('book-list'), data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Book.objects.count(), 2)