from rest_framework import serializers
from .models import Category, Book
from rate.serializers import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
class BookSerializer(serializers.ModelSerializer):
    
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), required=True)
    category_name = serializers.SerializerMethodField()
    author_name = serializers.SerializerMethodField()
    publisher = serializers.SerializerMethodField()
    rates = RateSerializer(read_only=True, many=True)
    class Meta:
        model = Book
        fields = (
                'id', 'name', 'img', 'description','author', 'author_name', 
                'category','category_name', 'price', 'language', 'no_of_page',
                'year_of_publication', 'total_number_of_book', 'publisher','rates'
        )
        
    def get_category_name(self, obj):
        return obj.category.name

    def get_author_name(self, obj):
        return f'{obj.author.f_name} {obj.author.l_name}'
    
    def get_publisher(slef, obj):
        return obj.publisher.username
    

    