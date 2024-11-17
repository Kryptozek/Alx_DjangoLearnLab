from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book# Import models from the current app
from .models import Library

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view for library details
class LibraryDetailView(DetailView):
    model = Library  # Specify the model to use for the view
    template_name = 'relationship_app/library_detail.html'  # Specify the template path
    context_object_name = 'library'  # Define the context object name for the template

