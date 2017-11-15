# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

from ..lr_app.models import Users
# Create your views here.
def default(request):
    """
    Route for the book review landing page
    """
    user = Users.objects.get(id=request.session['id'])
    return render(request, 'reviews_app/index.html', {'name': user.name})

def add(request):
    """
    Route for adding a book to the landing page
    """
    return render(request, 'reviews_app/add.html')

def viewBook(request, id):
    """
    Route for viewing a specific books info

    Args:
        id: book id for db query
    """
    return HttpResponse('specific book page for book ' + str(id))