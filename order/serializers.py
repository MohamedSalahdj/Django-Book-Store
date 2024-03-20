from rest_framework import serializers
from .models import Order, OrderItem, Cart, CartIetm

class OrderItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
    orderItems = serializers.SerializerMethodField(method_name="get_order_items", read_only=True)
    class Meta:
        model = Order
        fields = "__all__"

    def get_order_items(self,obj):
        order_items = obj.orderitems.all()
        serializer = OrderItemsSerializer(order_items,many=True)
        return serializer.data 
    

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartIetm
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    cart_item = CartItemSerializer(many=True)
    class Meta:
        model = Cart
        fields = '__all__'



