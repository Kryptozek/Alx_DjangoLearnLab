from rest_framework.generics import ListAPIView  # Import ListAPIView
from .models import Book
from .serializers import BookSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets  # Import ModelViewSet from DRF

class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing book instances.
    """
    queryset = Book.objects.all()  # Query for fetching all books
    serializer_class = BookSerializer  # Use the BookSerializer for serializing data
