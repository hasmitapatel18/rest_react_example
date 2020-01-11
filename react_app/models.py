from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse


# Create your models here.
class Collections(models.Model):
    name_of_collection = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name_of_collection


class Book(models.Model):
    collection = models.ForeignKey(Collections, default=None, null=True, on_delete = models.SET_DEFAULT)
    book_name = models.CharField(max_length=200,blank=True, null=True)
    book_author = models.CharField(max_length=200, blank=True, null=True)
    isbn = models.CharField(max_length=200, blank=True, null=True)
    year = models.PositiveSmallIntegerField(blank=True, null=True)

    def __str__(self):
        return self.book_name

    def __str__(self):
        return self.book_author

    class Meta:
        ordering=['book_author']


class Comment(models.Model):
    book = models.ForeignKey(Book, default=None, null=True, on_delete = models.SET_DEFAULT)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete = models.SET_DEFAULT)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.book

    def __str__(self):
        return self.content

    def user_name(self):
        full_name =self.user.get_full_name()
        return full_name

    class Meta:
        ordering = ('timestamp',)


class Rating(models.Model):
    book = models.ForeignKey(Book, default=None, null=True, on_delete = models.SET_DEFAULT)
    star_rating = models.PositiveSmallIntegerField(blank=True, null=True)




    
