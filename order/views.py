from django.shortcuts import render
from rest_framework import viewsets
from .models import Order,OrderItem
from .serializers import OrderSerializer
from rest_framework.pagination import PageNumberPagination
# Create your views here.




class OrderViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderSerializer
    pagination_class = PageNumberPagination
    pagination_class.page_size = 7


def add_to_cart(request, book_id):
    if request.user.is_authenticated():
        try:
            book = Book.objects.get(pk=book_id)
        except ObjectDoesNotExist:
            pass
        else:
            try:
                cart = Cart.objects.get(user=request.user, active=True)
            except ObjectDoesNotExist:
                cart = Cart.objects.create(
                    user = request.user
                )
                cart.save()
            cart.add_to_cart(book_id)
        return redirect('index')
    else:
        return redirect('index')


def remove_from_cart(request, book_id):
    if request.user.is_authenticated():
        try:
            book = Book.objects.get(pk=book_id)
        except ObjectDoesNotExist:
            pass
        else:
            cart = Cart.objects.get(user=request.user, active=True)
            cart.remove_from_cart(book_id)
        return redirect('cart')
    else:
        return redirect('index')


def cart(request):
    if request.user.is_authenticated():
        cart = Cart.objects.filter(user=request.user, active=True)
        orders = BookOrder.objects.filter(cart=cart)
        total=0
        count=0
        for order in orders:
            total += (order.book.price * order.quantity)
            count += order.quantity
        context = {
            'cart': orders,
            'total': total,
            'count': count,
        }
        return render(request, 'store/cart.html', context)
    else:
        return redirect('index')


def complete_order(request):
    if request.user.is_authenticated():
        cart= Cart.objects.get(user=request.user.id,active=True)
        orders= BookOrder.objects.filter(cart=cart)
        total = 0
        for order in orders:
            total += (order.book.price * order.quantity)
        message= "Success! Your order has been completed, and is being processed. Transaction made : $%s" %(total)
        cart.active =False
        cart.order_date= timezone.now()
        cart.save()
        context = {
            'message': message,
        }
        return render (request, 'store/order_complete.html',context)
    else:
        return redirect('index')