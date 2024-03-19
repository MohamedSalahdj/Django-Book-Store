from django.shortcuts import render
from book.models import Book
from .models import Order,OrderItem
from rest_framework.decorators import api_view,permission_classes
from .serializers import OrderItemsSerializer,OrderSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated 
from rest_framework import generics, status

# Create your views here.


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_order(request):
    user = request.user 
    data = request.data
    order_items = data['order_Items']

    if order_items and len(order_items) == 0:
       return Response({'error': 'No order recieved'},status=status.HTTP_400_BAD_REQUEST)
    else:
        total_amount = sum( item['price']* item['quantity'] for item in order_items)
        order = Order.objects.create(
            user = user,
            status= data['status'],
            quantity = data['quantity'],
            total_amount = total_amount,
        )
        for i in order_items:
            book = Book.objects.get(id=i['book'])
            item = OrderItem.objects.create(
                book= book,
                order = order,
                quantity = i['quantity'],
                price = i['price']
            )
            book.stock -= item.quantity
            book.save()
        serializer = OrderSerializer(order,many=False)
        return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_orders(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders,many=True)
    return Response({'orders':serializer.data})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_order(request,pk):
    order =get_object_or_404(Order, id=pk)

    serializer = OrderSerializer(order,many=False)
    return Response({'order':serializer.data})
































