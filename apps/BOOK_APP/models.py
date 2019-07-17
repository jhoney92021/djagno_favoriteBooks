from __future__ import unicode_literals
from django.db import models
from apps.LOGIN_APP.models import Users

class Authors(models.Model):
    fname = models.CharField(max_length=45, default='Apparently had no name')
    lname = models.CharField(max_length=45, default='Apparently had no name')
    notes = models.TextField(default='not much to say I guess')
    fan = models.ManyToManyField(Users, related_name='favorite_author')
    contributor = models.ForeignKey(Users, related_name='added_author', default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Books(models.Model):
    title = models.CharField(max_length=45, default='A title would go here, but you forgot')
    description = models.TextField(default='A description would go here, but you forgot')
    fan = models.ManyToManyField(Users, related_name='favorite_book')
    contributor = models.ForeignKey(Users, related_name='added_book', default=1)
    author = models.ManyToManyField(Authors, related_name='books')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)