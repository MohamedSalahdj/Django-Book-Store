from django.db import models
from book.models import Book
from django.contrib.auth.models import User
from users.models import CustomUser
from django.core.validators import MaxValueValidator, MinValueValidator 

class Rate(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,default=None)
    book=models.ForeignKey(Book,on_delete=models.CASCADE,related_name="book_review",default=None)
    review=models.TextField(null=True,blank=True)
    rate= models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    creation_date = models.DateField(auto_now_add=True)

