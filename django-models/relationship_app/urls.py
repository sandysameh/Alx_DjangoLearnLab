from django.urls import path
from .views import list_books
from .views import LibraryDetailView,LoginView,LogoutView
from . import views  # Import all views in a single line


urlpatterns = [
    path('books/',list_books,name="list_books"),
    path('library/<int:pk>/',LibraryDetailView.as_view(),name='library_detail'),
    path('login/',LoginView.as_view(template_name="relationship_app/login.html"),name="login"),

        path('logout/',LogoutView.as_view(template_name="relationship_app/logout.html"),name="logout"),

    path('register/',views.register,name="register"),
    path('admin/',views.admin_view,name="admin_view"),
    path('librarian/',views.librarian_view,name="librarian_view"),
        path('member/', views.member_view, name='member_view'),

    
    ]
