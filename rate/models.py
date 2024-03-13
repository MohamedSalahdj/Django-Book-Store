from django.db import models

# Create your models here.
class Rate(models.Model):
    #user
    #book
    review=models.TextField(null=True,blank=True)
    rate= models.IntegerField()
    creation_date = models.DateTimeField(auto_now_add=True)
