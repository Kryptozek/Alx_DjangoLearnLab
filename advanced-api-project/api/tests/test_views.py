from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from api.models import Author, Book

class BookAPITestCase(TestCase):
    def setUp(self):
        # Initialize API client
        self.client = APIClient()
        
        # Create an Author
        self.author = Author.objects.create(name="John Doe")
        
        # Create Books
        self.book1 = Book.objects.create(
            title="Book One", publication_year=2020, author=self.author
        )
        self.book2 = Book.objects.create(
            title="Book Two", publication_year=2021, author=self.author
        )
        
        # Endpoint URLs
        self.list_url = '/api/books/'
        self.detail_url = f'/api/books/{self.book1.id}/'

    def test_list_books(self):
        # Test retrieving all books
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_book(self):
        # Test creating a new book
        data = {
            "title": "Book Three",
            "publication_year": 2023,
            "author": self.author.id
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], "Book Three")

    def test_update_book(self):
        # Test updating an existing book
        data = {"title": "Updated Book One"}
        response = self.client.patch(self.detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Updated Book One")

    def test_delete_book(self):
        # Test deleting a book
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book1.id).exists())

    def test_filter_books_by_author(self):
        # Test filtering books by author
        response = self.client.get(self.list_url, {'author__name': 'John Doe'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_search_books(self):
        # Test searching books by title
        response = self.client.get(self.list_url, {'search': 'Book One'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_order_books(self):
        # Test ordering books by publication year
        response = self.client.get(self.list_url, {'ordering': 'publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], "Book One")
