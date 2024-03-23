from django.urls import path 
from .views import *
from .api import *


urlpatterns = [
    #^ for Author
    path('authors-all/', getall_authors, name='authors-all'),
    path('author/<int:id>', get_author_id, name='author-byid'),
    path('publisher-authors/', get_authors_by_publihser),
    
    #^ for Pubisher
    path('publishers-all/',PublisherListApi.as_view(), name='publishers-all'),
    path('publisher-details/<int:pk>',PublisherDetailsApi.as_view(), name='publisher-details'),
    path('add-publisher/',PublisherCreateApi.as_view(), name='add_publisher'),
    path('update-publisher/<int:pk>',PublisherUpdateApi.as_view(), name='update-publisher'),
    path('delete-publisher/<int:pk>',PublisherDeleteApi.as_view(), name='delte_publisher'),
]
