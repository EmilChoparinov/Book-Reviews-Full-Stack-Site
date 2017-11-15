# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

from models import Users

from django.contrib import messages

# Create your views here.
def default(request):
    """
    Route for rendering the login and registration page
    """
    return render(request, 'lr_app/lr.html')

def register(request):
    """
    Route for processing a login of a new user who does not have an account
    """
    if request.method == 'POST':
        response = Users.objects.addUser(request.POST)
        if len(response) != 0:
            for message in response:
                messages.warning(request, message)
            return redirect('/')
        request.session['id'] = Users.objects.get(email=request.POST['email']).id
    return redirect('/books')

def login(request):
    """
    Route for processing a login of a user who already has an account
    """
    if request.method == 'POST':
        response = Users.objects.validateLoginAttempt(request.POST)
        if len(response) != 0:
            for message in response:
                messages.warning(request,message)
            return redirect('/')
        request.session['id'] = Users.objects.get(email=request.POST['email']).id
    return redirect('/books')