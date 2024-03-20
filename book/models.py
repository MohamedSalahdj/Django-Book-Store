from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils import timezone

from account.models import Author
from users.models import CustomUser, CustomPublisher
from slugify import slugify_unicode
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(null=True, blank=True, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    @classmethod
    def create_categ(cls):
        cls.objects.create(name="Fiction")
        cls.objects.create(name="Nonfiction")
        cls.objects.create(name="Action and adventure")
        cls.objects.create(name="Art/architecture")
        cls.objects.create(name="Autobiography")
        cls.objects.create(name="Anthology")
        cls.objects.create(name="Biography")
        cls.objects.create(name="Classic")
        cls.objects.create(name="Cookbook")
        cls.objects.create(name="Dictionary")
        cls.objects.create(name="Guide")
        cls.objects.create(name="Humor")
        cls.objects.create(name="Horror")
        cls.objects.create(name="Journal")


book_language = (
    ('Arabic', 'Arabic'),
    ('English', 'English'),
)

class Book(models.Model):
    name = models.CharField(max_length=255)
    ISBN = models.CharField(max_length=255, unique=True)
    front_img = models.ImageField(upload_to='book/')
    back_img = models.ImageField(upload_to='book/')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    language = models.CharField(max_length=7, choices=book_language)
    no_of_page = models.IntegerField(null=True, blank=True)
    year_of_publication = models.DateField()
    total_number_of_book = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='book_category')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='book_author')
    publisher = models.ForeignKey(CustomPublisher, on_delete=models.CASCADE, related_name='publisher_book')
    slug  = models.SlugField(null=True, blank=True)
    
    def __str__(self):
        # return f'{ self.name} | By- {self.author.f_name} {self.author.l_name}'
        return self.name

    def save(self, *args, **kwargs):
        print(slugify_unicode(self.name))
        self.slug = slugify_unicode(self.name)
        super(Book, self).save(*args, **kwargs)

