from rest_framework import serializers
from .models import Orderlist

class OrderSerializer(serializers.ModelSerializer):
    total_price = serializers.ReadOnlyField()
    
    class Meta:
        model = Orderlist
        fields = '__all__'