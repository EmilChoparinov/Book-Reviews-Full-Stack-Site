# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

# Create your views here.
def default(request):
    """
    Route for rendering the login and registration page
    """
    return HttpResponse('Login and Reg page')

def register(request):
    """
    Route for processing a login of a new user who does not have an account
    """
    return HttpResponse('registering a user..')

def login(request):
    """
    Route for processing a login of a user who already has an account
    """
    return HttpResponse('logging in a user..')