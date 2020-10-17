from django.db import models
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

class Contacts(models.Model):
    Name = models.CharField(max_length = 20,default=None,null = True)
    Phone = models.IntegerField()
    is_spam = models.BooleanField(default=False)

class User_Table(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE,related_name = 'user_information')
    Name = models.CharField(max_length = 20,default=None,null = True)
    Phone = models.IntegerField(unique = True)
    is_spam = models.BooleanField(default = False)
    contacts = models.ManyToManyField(Contacts,related_name="Contacts")


# Create your models here.
