from django.urls import path 
from .views import *


urlpatterns = [
    path('authors-all/', getall_authors, name='authors-all'),
    path('author/<int:id>', get_author_id, name='author-byid')
]
