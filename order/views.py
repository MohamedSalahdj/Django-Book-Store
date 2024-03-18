from django.shortcuts import render
from rest_framework import viewsets
from .models import Order,OrderItem
from .serializers import OrderItemSerializer,OrderSerializer
from rest_framework.pagination import PageNumberPagination
# Create your views here.




class OrderViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    pagination_class = PageNumberPagination
    pagination_class.page_size = 7


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = PageNumberPagination
    pagination_class.page_size = 7       