from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated ,IsAdminUser
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from .models import Order, OrderItem, Cart, CartItem
from .serializers import OrderItemsSerializer, OrderSerializer, CartSerializer, CartItemSerializer
from book.models import Book, Category
from users.models import CustomUser, CustomPublisher


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_order(request):
    user = request.user 
    data = request.data
    order_items = data['order_Items']

    if order_items and len(order_items) == 0:
       return Response({'error': 'No order recieved'},status=status.HTTP_400_BAD_REQUEST)
    else:
        # total_amount = sum( item['price']* item['quantity'] for item in order_items)
        order = Order.objects.create(
            user = user,
            status= data['status'],
            quantity = data['quantity'],
            # total_amount = total_amount,
        )
        for i in order_items:
            book = Book.objects.get(id=i['book'])
            item = OrderItem.objects.create(
                book= book,
                order = order,
                quantity = i['quantity'],
                price = i['price']
            )
            book.total_number_of_book -= item.quantity
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
def get_order(request,id):
    order =get_object_or_404(Order, id=id)

    serializer = OrderSerializer(order,many=False)
    return Response({'order':serializer.data})



@api_view(['PUT'])
@permission_classes([IsAuthenticated,IsAdminUser])
def update_order(request,id):
    order =get_object_or_404(Order, id=id)
    order.status = request.data['status']
    order.save()
     
    serializer = OrderSerializer(order,many=False)
    return Response({'order':serializer.data})


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_order(request,id):
    order =get_object_or_404(Order, id=id) 
    order.delete()
      
    return Response({'msg': "order is deleted"})



class CartDetailCreateAPI(generics.GenericAPIView):
    serializer_class = CartSerializer
    
    def get(self, request, *args, **kwargs):
        customer = CustomUser.objects.get(id=self.kwargs['id'])
        cart, created = Cart.objects.get_or_create(customer=customer, status='InProgress')
        data = CartSerializer(cart).data
        return Response({'cart':data}) 
 
    def post(self, request, *args, **kwargs):
        customer = CustomUser.objects.get(id=self.kwargs['id'])
        book = Book.objects.get(id=request.data['book_id'])
        publisher = CustomPublisher.objects.get(id=request.data['CustomPublisher_id'])
        quantity = int(request.data['total_number_of_book'])
        
        cart = Cart.objects.get(customer=customer, status='InProgress')
        cart_item, created = CartItem.objects.get_or_create(cart=cart, book=book, publisher=publisher)
        cart_item.quantity = int(quantity)
        cart_item.total = round(int(quantity) * book.price, 2)
        cart_item.save()


        cart = Cart.objects.get(customer=customer, status='InProgress')
        data = CartSerializer(cart).data
        return Response({'msg':'book added successfully', 'cart':data})




    def delete(self, request, *args, **kwargs):
        customer = CustomUser.objects.get(id=self.kwargs['id'])
        cart_item = CartItem.objects.get(id=request.data['cart_item_id'])
        cart_item.delete()

        cart = Cart.objects.get(customer=customer, status='InProgress')
        data = CartSerializer(cart).data
        return Response({'msg':'book deleted successfully', 'cart':data})














