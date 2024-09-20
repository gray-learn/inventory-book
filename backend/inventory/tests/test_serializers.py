from django.test import TestCase
from inventory.models import Book
from inventory.serializers import BookSerializer

class BookSerializerTest(TestCase):
    def setUp(self):
        self.book_attributes = {
            "title": "Test Book",
            "author": "Test Author",
            "genre": "Test Genre",
            "publication_date": "2023-01-01",
            "isbn": "1234567890123"
        }
        self.book = Book.objects.create(**self.book_attributes)
        self.serializer = BookSerializer(instance=self.book)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'title', 'author', 'genre', 'publication_date', 'isbn']))
