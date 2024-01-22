from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass


class Book(models.Model):
    name = models.CharField(max_length=200)
    genre =  models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    

