from django.shortcuts import render,redirect,get_object_or_404
from .models import Library
from .models import Book

from django.views.generic.detail import DetailView

from django.contrib.auth import views
from django.contrib.auth import login
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import BookForm



# Create your views here.
def list_books(request):
    books = Book.objects.all()
    return render(request,'relationship_app/list_books.html',{'books':books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name='library'

class LoginView(views.LoginView):
    template_name="relationship_app/login.html"

class LogoutView(views.LogoutView):
    template_name= 'relationship_app/logout.html'

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("login")
    else:
        form = UserCreationForm()
    
    # This ensures that the form is rendered again if it's a GET request or if the form is invalid.
    return render(request, 'relationship_app/register.html', {'form': form})

@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books')
    else:
        form = BookForm()
    return render(request, 'relationship_app/book_form.html', {'form': form})

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('books')

    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/book_form.html', {'form': form})

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect('books')
    return render(request, 'relationship_app/book_confirm_delete.html', {'book': book})
