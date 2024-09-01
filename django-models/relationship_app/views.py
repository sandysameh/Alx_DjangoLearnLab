from django.shortcuts import render,redirect
from .models import Library
from .models import Book

from django.views.generic.detail import DetailView

from django.contrib.auth import views
from django.contrib.auth import login
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test



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

def Admin(user):
    return user.is_authenticated and user.profile.role == 'Admin'

def Librarian(user):
    return user.is_authenticated and user.profile.role == 'Librarian'

def Member(user):
    return user.is_authenticated and user.profile.role == 'Librarian'

@user_passes_test(Admin)
def AdminView(request):
    return HttpResponse("Welcome to the Admin view")

@user_passes_test(Librarian)
def LibrarianView(request):
    return HttpResponse("Welcome to the Librarian view")

@user_passes_test(Member)
def MemberView(request):
    return HttpResponse("Welcome to the Member view")
