from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils import timezone

#^ ----------------------------------------------  Author model -----------------------------------------
class Author(models.Model):
    """Author: reprsents the author of book and inherits from
        the base baseuser django model
        Attributes:
        * id: unique ideintifer
        * f_name: the author first name
        * l_name: the author last_name
        * Discreption: discreption and author bio
    """
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    biography = models.TextField(blank=True,null=True)

    @classmethod
    def create_author(cls, f_name, l_name, disc):
        cls.objects.create(f_name=f_name, l_name=l_name, biography=disc)
    
    def __str__(self):
        return f'{self.f_name} {self.l_name}'

#^ ----------------------------------------------  Publisher model -----------------------------------------

class Publisher(models.Model):
    name = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    certificate = models.FileField(upload_to='certificate/', blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    updatedate = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return f'{self.name, self.email, self.password,self.certificate}'
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Publisher, self).save(*args, **kwargs)
