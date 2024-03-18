from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    total_price = serializers.ReadOnlyField()
    
    class Meta:
        model = Order
        fields = '__all__'