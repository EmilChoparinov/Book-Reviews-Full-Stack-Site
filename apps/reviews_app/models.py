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
    def addBookAndReview(self, data):
        """
        Adds book and review information to database

        Args:
            data (request.POST): post data from a form

        Returns:
            list: a list of responses from the manager, if any response is given; that data is rejected
        """
    def addBook(self, data):
        pass
    
    def addReview(self, data):
        pass


class Books(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)

class Reviews(models.Model):
    review = models.TextField(null=True)
    user = models.ForeignKey(Users, related_name='reviews')
    book = models.ForeignKey(Books, related_name='reviews')