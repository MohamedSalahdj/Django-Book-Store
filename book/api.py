from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Category, Book
from .serializer import CategorySerializer, BookSerializer
from users.models import CustomPublisher
from rest_framework.pagination import PageNumberPagination
from django.db import models
from django.db.models import Avg, Sum
from rest_framework.views import APIView
from rest_framework import status


class CategoryListApi(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # lookup_field = 'slug'


class CategoryDetailsApi(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryCreateApi(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryUpdateApi(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDeleteApi(generics.DestroyAPIView):
    queryset = Category.objects.all()

class BookListApi(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def book_details(request, id):
    book = Book.objects.get(id=id)
    data = BookSerializer(book, context={'request':request}).data
    return Response({'book':data})
 

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def book_details_by_publisher(request, id):
    
    book = Book.objects.get(id=id)
    if request.user.id == book.publisher_id:
        data = BookSerializer(book, context={'request':request}).data
        return Response({'book':data})
    else:
        return Response({"Erorr": "You are not the book Publisher"})


class BookCreateApi(generics.CreateAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        print(self.request.user.id)      
        publisher = CustomPublisher.objects.get(id = self.request.user.id)
        serializer.save(publisher=publisher) 

class BookUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    print("called")
    def perform_update(self, serializer):
        print("called second")
        publisher = CustomPublisher.objects.get(id = self.request.user.id)
        serializer.save(publisher=publisher)   
    
    def patch(self, request, *args, **kwargs):
        print(request.data)
        return super().patch(request, *args, **kwargs)


class BookDeleteApi(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_publisher_books(request):
    """Return list of books created by the request publisher"""
    paginator = PageNumberPagination()
    publisher_books = Book.objects.filter(publisher_id = request.user.id)
    result_page = paginator.paginate_queryset(publisher_books, request)
    books_serializer = BookSerializer(result_page, many=True)
    return paginator.get_paginated_response(books_serializer.data)


#api for home page 
class BestRatedBooksAPIView(APIView):
    def get(self, request):
        best_books = Book.objects.annotate(avg_rating=Avg('book_review__rate')).order_by('-avg_rating')[:4]
        serializer = BookSerializer(best_books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class BestSellerBooksAPIView(APIView):
    def get(self, request):
        best_books = Book.objects.annotate(total_sold=Sum('order_book_item__quantity')).order_by('-total_sold')[:4]
        serializer = BookSerializer(best_books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def books_by_name(request,word):
        data = BookSerializer(Book.get_book_by_name(word), many=True).data
        return Response({'book':data})

@api_view(['GET'])
def related_books(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
        related_books = book.related_books(num=3) 
        serializer = BookSerializer(related_books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Book.DoesNotExist:
        return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)