from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(null=True, blank=True, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


book_language = (
    ('ar', 'Arabic'),
    ('en', 'English'),
    ('fr', 'French')
)

# class Book(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=6, decimal_places=2)
#     language = models.CharField(max_length=2, choices=book_language)
#     no_of_page = models.IntegerField()
#     year_of_publication = models.DateField()
#     total_number_of_book = models.IntegerField()
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='book_category')
#     author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='book_author')
#     publisher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='publisher_book')
#     slug  = models.SlugField(null=True, blank=True)

#     def save(self, *args, **kwargs):
#         self.slug = slugify(self.name)
#         super(Book, self).save(*args, **kwargs)