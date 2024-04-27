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
from .serializers import OrderItemsSerializer, OrderSerializer, CartSerializer, CartItemSerializer, PaymentSerializer
from book.models import Book, Category
from users.models import CustomUser, CustomPublisher, Address
from users.serializers import AddressSerializer
from rest_framework import status
from rest_framework.response import Response
from django.conf import settings
import stripe
from django.http import JsonResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import EmailMessage, send_mail
from django.template.loader import render_to_string






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

# class CreateOrderAPI(generics.GenericAPIView):

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
        success_url = "http://127.0.0.1:8000/" + '?success=true'
        cancel_url = "http://127.0.0.1:8000/" + '?canceled=true'
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









class CreateOrderAPI(generics.GenericAPIView):
    print("Called")
    def post(self, request, *args, **kwargs):
        customer = CustomUser.objects.get(id=self.kwargs['id'])
        print(customer)
        cart = Cart.objects.get(customer=customer, status='InProgress')
        cart_items = CartItem.objects.filter(cart=cart)
        YOUR_DOMAIN = "http://localhost:3000"
        print("THE EMAIL IS ", request.POST)
        address_data = {
            "country": request.data.get('country'),
            "city": request.data.get('city'),
            "street": request.data.get('street'),
            "phone": request.data.get('phone'),
            "user": customer.pk
        }
        print(type(address_data))
        # address_data = request.data.get('address')
        # address_data['user'] = customer.pk
        address_serializer = AddressSerializer(data=address_data)
        if address_serializer.is_valid():
            address_instance = address_serializer.save()
        else:
            print("SERIALIZER FAILED")
            return Response(address_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        new_order = Order.objects.create(
            user=customer,
            status='Received',
            total=cart.cart_total,
            delivery_address=address_instance,
        )

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
       
        stripe.api_key = settings.STRIPE_API_KEY_SECRET
        try:
            checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': int(cart.cart_total * 100), 
                        'product_data': {
                            'name': "Purchasing Books"
                        },
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            metadata={
                "order_id": 1
            },
            success_url = YOUR_DOMAIN  + '/?success=true/',
            cancel_url =  YOUR_DOMAIN + '/checkout/'
        )
            print(checkout_session)
            
            return redirect(checkout_session.url)
        except Exception as e:
            new_order.delete()
            return Response({'My error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
       

