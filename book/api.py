from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Category, Book
from .serializer import CategorySerializer, BookSerializer
from users.models import CustomPublisher
from rest_framework.pagination import PageNumberPagination


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
@permission_classes([IsAuthenticated])
def book_details(request, slug):
    book = Book.objects.get(slug=slug)
    if request.user.id == book.publisher_id:
        print("Authorsized")
        data = BookSerializer(book, context={'request':request}).data
        return Response({'book':data})
# def book_details(request, id):
#     book = Book.objects.get(id=id)
#     if request.user.id == book.publisher_id:
#         print("Authorsized")
#     data = BookSerializer(book, context={'request':request}).data
#     return Response({'book':data})


class BookCreateApi(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        publisher = self.request.user
        serializer.save(publisher=publisher)    

class BookUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        publisher = self.request.user
        serializer.save(publisher=publisher)   


class BookDeleteApi(generics.DestroyAPIView):
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


