from django.shortcuts import render
from book.models import Book
from .models import Order,OrderItem
from rest_framework.decorators import api_view,permission_classes
from .serializers import OrderItemsSerializer,OrderSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated ,IsAdminUser
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from .models import Order, OrderItem, Cart, CartItem
from .serializers import OrderItemsSerializer, OrderSerializer, CartSerializer, CartItemSerializer
from book.models import Book, Category
from users.models import CustomUser, CustomPublisher
from rest_framework import status




@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_publisher_orders(request, publisher_id):
    orders = Order.objects.filter(orderitems__publisher_id=publisher_id)
    serializer = OrderSerializer(orders, many=True)
    return Response({'orders': serializer.data})

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_customer_orders(request, customer_id):
    orders = Order.objects.filter(user_id=customer_id)
    serializer = OrderSerializer(orders, many=True)
    return Response({'orders': serializer.data})



class CreateOrderAPI(generics.GenericAPIView):
    
    def get(self, request, *args, **kwargs):
        customer = CustomUser.objects.get(id=self.kwargs['id'])
        cart = Cart.objects.get(customer=customer, status='InProgress')
        cart_items = CartItem.objects.filter(cart=cart)
        # address_id
        # user_address

        new_order = Order.objects.create(
            user = customer,
            status = 'Received',
            total = cart.cart_total
            # customer_address
            
        )

        for item in cart_items:
            book = Book.objects.get(id=item.book.id)
            OrderItem.objects.create(
                book = book , 
                publisher = item.publisher,
                order = new_order , 
                price = book.price , 
                quantity = item.quantity , 
                total = round(item.quantity * book.price, 2)
            )

        cart.status = 'Completed'
        cart.save()
        return Response({'msg':'order was created successfully'},status=status.HTTP_201_CREATED)


@api_view(['PUT'])
@permission_classes([IsAuthenticated, IsAdminUser])
def update_order(request,id):
    order = get_object_or_404(Order, id=id)
    order.status = request.data['status']
    order.save()
     
    serializer = OrderSerializer(order, many=False)
    return Response({'order': serializer.data})


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

        return Response({'msg' : 'book added successfully', 'cart':data})

    def delete(self, request, *args, **kwargs):
        customer = CustomUser.objects.get(id=self.kwargs['id'])
        cart_item = CartItem.objects.get(id=request.data['cart_item_id'])
        cart_item.delete()

        cart = Cart.objects.get(customer=customer, status='InProgress')
        data = CartSerializer(cart).data
        return Response({'msg':'book deleted successfully', 'cart':data})














