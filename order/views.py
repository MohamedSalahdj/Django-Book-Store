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




































# class OrderListCreateView(generics.ListCreateAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer
#     permission_classes = [IsAuthenticated]

#     def create(self, request, *args, **kwargs):
#         user = request.user
#         data = request.data
#         order_items = data.get('order_items', [])

#         if not order_items:
#             return Response({'error': 'No order received'}, status=status.HTTP_400_BAD_REQUEST)

#         total_amount = sum(item['price'] * item['quantity'] for item in order_items)
#         order = Order.objects.create(
#             user=user,
#             city=data['city'],
#             zip_code=data['zip_code'],
#             street=data['street'],
#             phone_no=data['phone_no'],
#             country=data['country'],
#             total_amount=total_amount,
#         )

#         for item in order_items:
#             product = Product.objects.get(id=item['product'])
#             order_item = OrderItem.objects.create(
#                 product=product,
#                 order=order,
#                 name=product.name,
#                 quantity=item['quantity'],
#                 price=item['price']
#             )
#             product.stock -= order_item.quantity
#             product.save()

#         serializer = self.get_serializer(order)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# class OrderRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer
#     permission_classes = [IsAuthenticated]

#     def update(self, request, *args, **kwargs):
#         partial = kwargs.pop('partial', False)
#         instance = self.get_object()
#         serializer = self.get_serializer(instance, data=request.data, partial=partial)
#         serializer.is_valid(raise_exception=True)
#         self.perform_update(serializer)

#         if getattr(instance, '_prefetched_objects_cache', None):
#             instance._prefetched_objects_cache = {}

#         return Response(serializer.data)

#     def perform_update(self, serializer):
#         status_value = self.request.data.get('status')
#         if status_value:
#             serializer.save(status=status_value)
#         else:
#             serializer.save()

















# class OrderProcessView(generics.UpdateAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer
#     permission_classes = [IsAuthenticated, IsAdminUser]

#     def perform_update(self, serializer):
#         status_value = self.request.data.get('status')
#         serializer.save(status=status_value)


# class OrderDeleteView(generics.DestroyAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer
#     permission_classes = [IsAuthenticated]

#     def perform_destroy(self, instance):
#         instance.delete()
#         return Response({'detail': 'Order is deleted'}, status=status.HTTP_204_NO_CONTENT)






































# class OrderViewSet(viewsets.ModelViewSet):
#     queryset = OrderItem.objects.all()
#     serializer_class = OrderItemSerializer
#     pagination_class = PageNumberPagination
#     pagination_class.page_size = 7


# class OrderViewSet(viewsets.ModelViewSet):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer
#     pagination_class = PageNumberPagination
#     pagination_class.page_size = 7 







# class ProductOrderCreate(CreateAPIView):
#     queryset = models.ProductOrder.objects.all()
#     serializer_class = ProductOrderSerializer
#     permission_classes = [IsAuthenticated,IsCustomer]

#     def perform_create(self, serializer):

#         order = serializer.save()

#         subject = "Potwierdzenie"
#         contents = f"Zamównie nr.{order.id} zostało poprawnie złożone"
#         email = self.request.user.email

#         send_mail(
#             subject,
#             contents,
#             'company_email@example.com',
#             [email],
#             fail_silently=False,
#         )   
# class ProductOrderList(ListAPIView):
#     queryset = models.ProductOrder.objects.all()
#     serializer_class = ProductOrderListSerializer