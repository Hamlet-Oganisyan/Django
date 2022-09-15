from django.shortcuts import render, redirect
from django.urls import reverse
from books.models import Book


def index(request):
    return redirect(reverse('books'))


def books_view(request):
    template = 'books/books_list.html'
    context = {'books': Book.objects.all()}
    return render(request, template, context)


def pub_date_view(request, date):
    template = 'books/books_list.html'
    book = Book.objects.filter(pub_date=date)
    prev = Book.objects.filter(pub_date__gt=date).values('pub_date').first()
    next = Book.objects.filter(pub_date__lt=date).values('pub_date').first()
    context = {'books': book,
               'prev': prev,
               'next': next,
               }
    return render(request, template, context)