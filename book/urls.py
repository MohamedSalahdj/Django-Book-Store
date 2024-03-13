from django.urls import path 
from .api import *


urlpatterns = [
    path('list-cateory/',CategoryListApi.as_view(), name='category_list'),
    path('cateory-details/<int:pk>/',CategoryDetailsApi.as_view(), name='category_detail'),
    path('add-category/',CategoryCreateApi.as_view(), name='add_category'),
    path('delete-category/<int:pk>',CategoryDeleteApi.as_view(), name='delte_category'),

    path('list-book/', BookListApi.as_view(), name='list_book'),
    path('<slug:slug>-book/details',  book_details, name='book_details'),
    path('add-book/', BookCreateApi.as_view(), name='add_book'),    

]
