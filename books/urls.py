from django.urls import path
from . import views

from django.conf import settings 
from django.conf.urls.static import static 

from .views import book_detail, books_list, random_list, CreateBook, UpdateBook, DeleteBook, new_books_list

# app_name = 'books'

urlpatterns = [
    path('', views.books_list, name='books'),
    path('books/', views.new_books_list, name='new_books_list'),
    path('book_detail/<int:id>/<slug:slug>', views.book_detail, name = 'book_detail'),
    path('random_list', views.random_list, name='random_list'),
    path('books/new_book/', CreateBook.as_view(), name='new_book'),
    path('books/<int:pk>/book_delete/', DeleteBook.as_view(), name='book_delete'),
    path('books/<int:pk>/book_edit/', UpdateBook.as_view(), name='book_edit'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)