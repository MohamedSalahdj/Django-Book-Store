from django.shortcuts import render
from rest_framework import viewsets
from .models import Orderlist
from .serializers import OrderSerializer
from rest_framework.pagination import PageNumberPagination
# Create your views here.




class OrderViewSet(viewsets.ModelViewSet):
    queryset = Orderlist.objects.all()
    serializer_class = OrderSerializer
    pagination_class = PageNumberPagination
    pagination_class.page_size = 7


