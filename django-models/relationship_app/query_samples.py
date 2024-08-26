import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

author = Author.objects.create(name='J.K. Rowling')
book = Book.objects.create(title='Harry Potter and the Philosopher\'s Stone', author=author)
library = Library.objects.create(name='Central Library')
library.books.add(book)
librarian = Librarian.objects.create(name='John Doe', library=library)


# Query 1: Query all books by a specific author
author_name = 'J.K. Rowling'
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)
print(f'Books by {author_name}:')
for book in books_by_author:
    print(f'- {book.title}')

# Query 2: List all books in a library
library_name = 'Central Library'
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()
print(f'Books in {library_name}:')
for book in books_in_library:
    print(f'- {book.title}')

# Query 3: Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library_name)
print(f'Librarian of {library_name}: {librarian.name}')
