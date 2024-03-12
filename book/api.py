from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .models import Category
from .serializer import CategorySerializer

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
