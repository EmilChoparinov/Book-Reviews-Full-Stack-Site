# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ..lr_app.models import Users

from django.db import models


# Create your models here.
class Books_ReviewsManager(models.Manager):
    """
    Manager Class for Class Books and Class Reviews

    Attributes:
        addInfo (data): adds either info of a book or review to database
    """
    def addBook(self, data, u_id):
        """
        Adds a book to the database

        Args:
            data (request.POST): post data from a form
            u_id (int): user id who submitted the for

        Returns:
            list: a list of responses from the manager, if any response is given; that data is rejected
        """
        response = []
        if not data['title']:
            response.append('Book must have a title!')
        if not data['author']:
            response.append('Book must have an author')
        if not data['review']:
            response.append('Book must have at least one review to be added!')
        if 'rating' not in data:
            response.append('Book must have a rating!')   
        if len(response) == 0:
            if len(Authors.objects.filter(name=data['author'])) == 0:
                Authors.objects.create(name=data['author'])

            this_book = Books.objects.create(
                title = data['title'],
                author = Authors.objects.get(name=data['author'])
            )
            Reviews.objects.create(
                review = data['review'],
                rating = data['rating'],
                user = Users.objects.get(id=u_id),
                book = this_book
            )
        return response
    
    def addReview(self, data, b_id, u_id):
        """
        Adds a review of a book to the database

        Args:
            data (request.POST): post data from a form
            b_id (int): book id of the id for the book who will get reviewed
            u_id (int): user id of the id for the user who will submit the review

        Returns:
            list: a list of responses from the manager, if any response is given; that data is rejected
        """
        response = []
        if not data['review']:
            response.append('Must have some writing in the review box!')
        if 'rating' not in data:
            response.append('The book must have a rating!')
        if len(response) == 0:
            this_review = Reviews.objects.create(
                review = data['review'],
                rating = data['rating'],
                user = Users.objects.get(id=u_id),
                book = Books.objects.get(id=b_id)
            )
        return response

    def getByLast(self, n):
        """
        Gets the reviews sorted by recent for easy display
        
        Args:
            n (int): number of reviews to return
        Returns:
            list: last three reviews
        """
        n = Reviews.objects.all().order_by('-id')[:n]
        for i in n:
            i.rating = range(i.rating)
        return n


class Authors(models.Model):
    name = models.CharField(max_length=255)

class Books(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Authors, related_name='books')
    objects = Books_ReviewsManager()

class Reviews(models.Model):
    review = models.TextField(null=True)
    rating = models.IntegerField()
    user = models.ForeignKey(Users, related_name='reviews')
    book = models.ForeignKey(Books, related_name='reviews')
    objects = Books_ReviewsManager()