from django.test import TestCase
from inventory.models import Book

class BookModelTest(TestCase):
    def setUp(self):
        Book.objects.create(
            title="Test Book",
            author="Test Author",
            genre="Test Genre",
            publication_date="2023-01-01",
            isbn="1234567890123"
        )

    def test_book_creation(self):
        book = Book.objects.get(isbn="1234567890123")
        self.assertEqual(book.title, "Test Book")
        self.assertEqual(book.author, "Test Author")