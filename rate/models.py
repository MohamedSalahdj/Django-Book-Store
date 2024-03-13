from django.db import models
# from book.models import Book
from django.contrib.auth.models import User

class Rate(models.Model):
    #user
    #book
    review=models.TextField(null=True,blank=True)
    rate= models.IntegerField()
    creation_date = models.DateTimeField(auto_now_add=True)
