# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

from ..lr_app.models import Users
from ..reviews_app.models import Books, Reviews, Authors
from django.contrib import messages
# Create your views here.
def default(request):
    """
    Route for the book review landing page
    """
    context ={
        'user': Users.objects.get(id=request.session['id']),
        'reviews': Reviews.objects.getByLast(3),
        'books': Books.objects.all().order_by('-id')
    }
    user = Users.objects.get(id=request.session['id'])
    return render(request, 'reviews_app/index.html', context)

def add_book(request):
    """
    Route for adding a book to the landing page
    """
    context = {
        'authors': Authors.objects.all(),
    }
    return render(request, 'reviews_app/add.html', context)

def add_book_process(request):
    """
    Route for processing a book being added to the database
    """
    if request.method == 'POST':
        response = Books.objects.addBook(request.POST, request.session['id'])
        if len(response) != 0:
            for message in response:
                messages.warning(request, message)
            return redirect('/books/add')
    return redirect('/books')

def viewBook(request, b_id):
    """
    Route for viewing a specific books info

    Args:
        id: book id for db query
    """
    book = Books.objects.get(id=b_id)
    reviews = book.reviews.order_by('-id')
    for review in reviews:
        review.rating = range(review.rating)
    context = {
        'book': book,
        'reviews': reviews
    }
    return render(request, 'reviews_app/book.html', context)

def review_process(request):
    """
    Route for processing a review being added to the database
    """
    if request.method == 'POST':
        response = Reviews.objects.addReview(request.POST, request.POST['b_id'], request.session['id'])
    if len(response) != 0:
        for message in response:
            messages.warning(request, message)
    return redirect('/books/' + str(request.POST['b_id']))