from django.shortcuts import render, get_object_or_404
from .models import Books
import random
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import BookForm


# Create your views here.

def books_list(request):
    books = Books.objects.all()
    return render(request,'books_list.html', {'books': books})

def new_books_list(request):
    books = Books.objects.filter(image=True)
    return render(request, 'new_books_list.html', {'books': books})

def book_detail(request):
    book = get_object_or_404(Books)
    return render(request, 'book_detail.html', {'book_detail': book})

def random_list(request):
    random_list = list(Books.objects.all())
    random_list = random.sample(random_list, 3)
    return render(request, 'random_list.html', {'random_list': random_list})

class CreateBook(CreateView):
    form_class = BookForm
    template_name = 'new_book.html'
    success_url = reverse_lazy('books:books_list')


class UpdateBook(UpdateView):
    model = Books
    form_class = BookForm
    books = Books.objects.all()
    template_name = 'book_edit.html'
    success_url = reverse_lazy('books:new_books_list')



class DeleteBook(DeleteView):
    model = Books
    template_name = 'book_delete.html'
    success_url = reverse_lazy('books:new_books_list')






# def frontpage(request):
#     products = list(Product.objects.all())

#     products = random.sample(products, 9)

#     return render(request, 'front-page.html', {'products': products})



