from bookshelf.models import Author, Book, Library, Librarian

# Query all books by a specific author
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return Book.objects.filter(author=author)

# List all books in a library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

# Retrieve the librarian for a library
def librarian_of_library(library_name):
    # Fetch the Library object
    library = Library.objects.get(name=library_name)
    # Use Librarian.objects.get with a filter on the library field
    return Librarian.objects.get(library=library)


