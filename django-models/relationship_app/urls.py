from django.urls import path
from .views import list_books
from .views import LibraryDetailView,LoginView,LogoutView
from . import views  # Import all views in a single line


urlpatterns = [
    path('books/',list_books,name="books"),
    path('library/<int:pk>/',LibraryDetailView.as_view(),name='library_detail'),
    path('login/',LoginView.as_view(template_name="relationship_app/login.html"),name="login"),

        path('logout/',LogoutView.as_view(template_name="relationship_app/logout.html"),name="logout"),

    path('register/',views.register,name="register"),

        path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:pk>/', views.delete_book, name='delete_book'),

    ]
