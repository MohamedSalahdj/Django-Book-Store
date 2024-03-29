from django.urls import path 
from .api import *


urlpatterns = [
    path('list-cateory/',CategoryListApi.as_view(), name='category_list'),
    path('cateory-details/<int:pk>/',CategoryDetailsApi.as_view(), name='category_detail'),
    path('add-category/',CategoryCreateApi.as_view(), name='add_category'),
    path('delete-category/<int:pk>',CategoryDeleteApi.as_view(), name='delte_category'),

    path('list-book/', BookListApi.as_view(), name='list_book'),
    path('get-publisher-books/',get_publisher_books, name='publisher_books'),
    path('<int:id>-book/details',  book_details, name='book_details'),
    path('<int:id>-publisherbook/details', book_details_by_publisher),
    path('add-book/', BookCreateApi.as_view(), name='add_book'),    
    path('<int:pk>-book/update',  BookUpdateApi.as_view(), name='book_details'),
    path('<int:pk>-book/delete', BookDeleteApi.as_view(), name='delete_book'),
    path('<str:word>-book/search',books_by_name, name='book_search'),
    # home page api
    path('best-rated-books/', BestRatedBooksAPIView.as_view(), name='best_rated_books'),
    path('best-seller-books/', BestSellerBooksAPIView.as_view(), name='best_seller_books'),
    path('<int:book_id>/related-books/', related_books)
]
