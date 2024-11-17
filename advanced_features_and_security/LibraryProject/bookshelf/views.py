from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.shortcuts import  redirect
from .models import Book
from .forms import BookSearchForm

@permission_required('app_name.can_view', raise_exception=True)
def view_instance(request, instance_id):
    # Logic to view an instance
    pass

@permission_required('app_name.can_create', raise_exception=True)
def create_instance(request):
    # Logic to create an instance
    pass

@permission_required('app_name.can_edit', raise_exception=True)
def edit_instance(request, instance_id):
    # Logic to edit an instance
    pass

@permission_required('app_name.can_delete', raise_exception=True)
def delete_instance(request, instance_id):
    # Logic to delete an instance
    pass


def book_list(request):
    """
    View to display a list of all books.
    """
    books = Book.objects.all()  # Fetch all books from the database
    return render(request, 'bookshelf/book_list.html', {'books': books})


def book_search(request):
    if request.method == "GET":
        form = BookSearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['search_query']
            books = Book.objects.filter(title__icontains=query)
            return render(request, 'bookshelf/book_list.html', {'books': books, 'form': form})
    else:
        form = BookSearchForm()
    return render(request, 'bookshelf/book_list.html', {'form': form})



