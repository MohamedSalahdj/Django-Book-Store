from django.shortcuts import render
from rest_framework import viewsets
from .models import Orderlist
from .serializers import OrderSerializer
# Create your views here.




class OrderViewSet(viewsets.ModelViewSet):
    queryset = Orderlist.objects.all()
    serializer_class = OrderSerializer


