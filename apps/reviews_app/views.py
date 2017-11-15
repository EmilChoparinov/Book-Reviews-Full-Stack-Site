# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

# Create your views here.
def default(request):
    """
    Route for the book review landing page
    """
    return HttpResponse('default page')

def add(request):
    """
    Route for adding a book to the landing page
    """
    return HttpResponse('add a book page')

def viewBook(request, id):
    """
    Route for viewing a specific books info

    Args:
        id: book id for db query
    """
    return HttpResponse('specific book page for book ' + str(id))