from django.db import models
from django.contrib.auth.models import User

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
