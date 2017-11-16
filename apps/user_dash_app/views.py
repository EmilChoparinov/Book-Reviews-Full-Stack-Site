# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

from ..lr_app.models import Users
from ..reviews_app.models import Books, Reviews, Authors

# Create your views here.
def showUser(request, u_id):
    user = Users.objects.get(id=u_id)
    reviews = user.reviews.order_by('-id')
    for review in reviews:
        review.rating = range(review.rating)
    context = {
        'user': user,
        'reviews': reviews,
        'books': reviews
    }
    return render(request, 'user_dash_app/user.html', context)