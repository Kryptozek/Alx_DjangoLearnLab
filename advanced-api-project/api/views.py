from rest_framework import generics
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from api.models import Author, Book

# List View for Books
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Public read-only access
       
     # Enable filtering, searching, and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Define fields for filtering
    filterset_fields = ['title', 'author__name', 'publication_year']

    # Define fields for search functionality
    search_fields = ['title', 'author__name']

    # Define fields for ordering
    ordering_fields = ['title', 'publication_year']

# Create View for Books
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can create

# Detail View for a Single Book
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Public read-only access

# Update View for a Book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can update

# Delete View for a Book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can delete


class BookAPITestCase(TestCase):
    def setUp(self):
        # Initialize API client
        self.client = APIClient()
        
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
        )
        
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

    def test_authenticated_create_book(self):
        # Login the user
        self.client.login(username='testuser', password='testpassword')
        
        # Test creating a new book
        data = {
            "title": "Book Three",
            "publication_year": 2023,
            "author": self.author.id
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], "Book Three")

    def test_unauthenticated_create_book(self):
        # Test creating a book without authentication
        data = {
            "title": "Book Four",
            "publication_year": 2023,
            "author": self.author.id
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_delete_book(self):
        # Login the user
        self.client.login(username='testuser', password='testpassword')
        
        # Test deleting a book
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book1.id).exists())

    def test_unauthenticated_delete_book(self):
        # Test deleting a book without authentication
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
