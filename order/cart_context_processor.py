from .models import Cart, CartIetm

def get_cart_data(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(customer=request.user, status='InProgress')
        cart_detail = CartIetm.objects.filter(cart=cart)
        return {'cart_data': cart, 'cart_detail_data': cart_detail}
    else:
        return {}