from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated ,IsAdminUser
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from .models import Order, OrderItem, Cart, CartItem
from .serializers import OrderItemsSerializer, OrderSerializer, CartSerializer, CartItemSerializer, PaymentSerializer
from book.models import Book, Category
from users.models import CustomUser, CustomPublisher, Address
from users.serializers import AddressSerializer
from rest_framework import status
from django.conf import settings
import stripe


# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def add_order(request):
#     user = request.user 
#     data = request.data

#     order_items = data['order_Items']

#     if order_items and len(order_items) == 0:
#        return Response({'error': 'No order recieved'},status=status.HTTP_400_BAD_REQUEST)
#     else:
#         # total_amount = sum( item['price']* item['quantity'] for item in order_items)
#         order = Order.objects.create(
#             user = user,
#             status= data['status'],
#             quantity = data['quantity'],
#             # total_amount = total_amount,
#         )
#         for i in order_items:
#             book = Book.objects.get(id=i['book'])
#             item = OrderItem.objects.create(
#                 book= book,
#                 order = order,
#                 quantity = i['quantity'],
#                 price = i['price']
#             )
#             book.total_number_of_book -= item.quantity
#             book.save()
#         serializer = OrderSerializer(order,many=False)
#         return Response(serializer.data)

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def get_orders(request):
#     orders = Order.objects.all()
#     serializer = OrderSerializer(orders,many=True)
#     return Response({'orders':serializer.data})


# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def get_order(request,id):
#     order =get_object_or_404(Order, id=id)

#     serializer = OrderSerializer(order,many=False)
#     return Response({'order':serializer.data})





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

    def post(self, request, *args, **kwargs):
        customer = CustomUser.objects.get(id=self.kwargs['id'])
        print(customer)
        cart = Cart.objects.get(customer=customer, status='InProgress')
        cart_items = CartItem.objects.filter(cart=cart)
        
    
        address_data = request.data.get('address')
        address_data['user'] = customer.pk
        address_serializer = AddressSerializer(data=address_data)
        if address_serializer.is_valid():
            address_instance = address_serializer.save()
        else:
            return Response(address_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        new_order = Order.objects.create(
            user=customer,
            status='Received',
            total=cart.cart_total,
            delivery_address=address_instance,
        )
        
        stripe.api_key = settings.STRIPE_API_KEY_SECRET
        payment_data = request.data.get('payment')
        
        try:
            payment_intent = stripe.PaymentIntent.create(
                amount=int(cart.cart_total * 100),  
                currency='usd',
                description='Payment for Order #{}'.format(new_order.pk),
                metadata={'order_id': new_order.pk},
            )
        except stripe.error.StripeError as e:
            new_order.delete()
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        payment_data['order'] = new_order.pk
        payment_serializer = PaymentSerializer(data=payment_data)

        if payment_serializer.is_valid():
            payment_instance = payment_serializer.save()
            new_order.payment_order.add(payment_instance)
        else:
            new_order.delete()
            return Response(payment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        for item in cart_items:
            book = Book.objects.get(id=item.book.id)
            OrderItem.objects.create(
                book=book,
                publisher=item.publisher,
                order=new_order,
                price=book.price,
                quantity=item.quantity,
                total=round(item.quantity * book.price, 2)
            )
            book.total_number_of_book -= item.quantity
            book.save()

        cart.status = 'Completed'
        cart.save()

        return Response({'msg': 'Order was created successfully'}, status=status.HTTP_201_CREATED)


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
        
        if quantity > book.total_number_of_book:
            return Response({'error': 'Quantity exceeds available stock'}, status=status.HTTP_400_BAD_REQUEST)
        
        cart = Cart.objects.get(customer=customer, status='InProgress')
        cart_item, created = CartItem.objects.get_or_create(cart=cart, book=book, publisher=publisher)
        
        cart_item.quantity = int(quantity)
        cart_item.total = round(int(quantity) * book.price, 2)
        cart_item.save()
        
        cart = Cart.objects.get(customer=customer, status='InProgress')
        data = CartSerializer(cart).data

        return Response({'msg' : 'Book added successfully', 'cart': data})

    def delete(self, request, *args, **kwargs):
        customer = CustomUser.objects.get(id=self.kwargs['id'])
        cart_item = CartItem.objects.get(id=request.data['cart_item_id'])
        cart_item.delete()

        cart = Cart.objects.get(customer=customer, status='InProgress')
        data = CartSerializer(cart).data
        return Response({'msg':'book deleted successfully', 'cart':data})














