from django.shortcuts import render, get_object_or_404
from .models import Books

# Create your views here.

def books_list(request):
    books = Books.objects.all()
    return render(request,'books_list.html', {'books': books})


def book_detail(request):
    book = get_object_or_404(Books)
    return render(request, 'book_detail.html', {'book_detail': book})



