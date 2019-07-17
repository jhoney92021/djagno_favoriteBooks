from __future__ import unicode_literals
from django.db import models
import re, bcrypt, datetime


class Manager(models.Manager):
    def validator(self, postData):
        errors = {}
       

        emailFormat = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') # all characters, all characters, only 3 letters
        #GIVEN NAME FORMAT ERRORS
        if len(postData['fname']) < 2: #CHECK FOR FNAME LEN
            errors['fname'] = 'Wrong Again Bob, fname to short'
        if len(postData['lname']) < 2: #CHECK FOR LNAME LEN
            errors['lname'] = 'Wrong Again Bob, lname to short'
        #USERNAME ERRORS
        if len(postData['username']) < 2: #CHECK FOR USERNAME LEN
            errors['username'] = 'Wrong Again Bob, username to short'
        if postData['username'] in Users.objects.filter(username=postData['username']): #CHECK FOR USERNAME UNIQUENESS
            errors['username'] = 'Wrong Again Bob, fname taken'
        #EMAIL ERRORS
        if not emailFormat.match(postData['email']): #CHECK FOR EMAIL FORMAT
            errors['email'] = 'cmon, use an actualy email......'
        if postData['email'] in Users.objects.filter(email=postData['email']): #CHECK FOR EMAIL UNIQUENESS
            errors['email'] = 'Wrong Again Bob, email taken'
        #PASSWORD ERRORS
        if len(postData['password']) < 1 :#CHECK FOR PASSWORD FORMAT
            errors['passlen'] = 'Passwords field cannot be empty'
        if postData['password'] != postData['confirmation']: #CHECK FOR PASSWORD MATCH
            errors['password'] = 'Wrong Again Bob, passwords do not match'

        return errors

    #END VALIDATOR
    #END VALIDATOR
    #BEGIN LOGIN VALIDATOR
    #BEGIN LOGIN VALIDATOR

    def loginVal(self, postData):
        errors = {'logFail': 'YEARRRG'}
        if len(postData['password']) < 1 :
            errors['passlen'] = 'Passwords field cannot be empty'
        if len(postData['email']) < 1 :
            errors['emaillen'] = 'Email field cannot be empty'        

        return errors

class Users(models.Model):
    fname = models.CharField(max_length=20, default='A person with no name apparently')
    lname = models.CharField(max_length=20, default='A person with no name apparently')
    username = models.CharField(max_length=20, default='not a required field')
    birthday = models.DateField(default= datetime.date.today)
    email = models.CharField(max_length=80, default='Seriously, no email? it is 2019 get with it man')
    password = models.CharField(max_length=8)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = Manager()
