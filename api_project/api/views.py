from rest_framework.generics import ListAPIView  # Import ListAPIView
from rest_framework import generics 
from .models import Book
from .serializers import BookSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets  # Import ModelViewSet from DRF
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.permissions import IsAdminUser

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing book instances.
    """
    queryset = Book.objects.all()  # Query for fetching all books
    serializer_class = BookSerializer  # Use the BookSerializer for serializing data
    permission_classes = [IsAdminUser]
    permission_classes = [IsAuthenticated]
