from rest_framework import serializers
from .models import Order, OrderItem, Cart, CartItem, Payment
from book.serializer import BookSerializer


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class OrderItemsSerializer(serializers.ModelSerializer):
    book = BookSerializer()
    total_price = OrderItem.total_price
    class Meta:
        model = OrderItem
        fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
    # orderItems = serializers.SerializerMethodField(method_name="get_order_items", read_only=True)
    orderitems = OrderItemsSerializer(many=True)
    class Meta:
        model = Order
        fields = "__all__"

    def get_order_items(self,obj):
        order_items = obj.orderitems.all()
        serializer = OrderItemsSerializer(order_items,many=True)
        return serializer.data 
    

class CartItemSerializer(serializers.ModelSerializer):
    # book = serializers.StringRelatedField()
    book = BookSerializer()
    class Meta:
        model = CartItem
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemSerializer(many=True)
    total_price_cart = serializers.SerializerMethodField()
    class Meta:
        model = Cart
        fields = '__all__'

    def get_total_price_cart(self, obj):
        total = sum(item.quantity * item.book.price for item in obj.cart_items.all())
        return round(total, 2)