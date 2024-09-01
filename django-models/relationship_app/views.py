from django.shortcuts import render,redirect
from .models import Library
from .models import Book

from django.views.generic.detail import DetailView

from django.contrib.auth import views,login
from django.contrib.auth.forms import UserCreationForm



# Create your views here.
def list_books(request):
    books = Book.objects.all()
    return render(request,'relationship_app/list_books.html',{'books':books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name='library'

class CustomLoginView(views.LoginView):
    template_name="relationship_app/login.html"

class CustomLogoutView(views.LogoutView):
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

