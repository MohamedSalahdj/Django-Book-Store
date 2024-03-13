from rest_framework import serializers
from .models import Category, Book

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

# class BookSerializer(serializers.ModelSerializer):
#     category_names = serializers.SerializerMethodField()  

#     class Meta:
#         model = Book
#         exclude = ('publisher', 'category')

#     def get_category_names(self, obj):
#         return obj.category.name 
        

class BookSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()
    publisher = serializers.SerializerMethodField()
    class Meta:
        model = Book
        fields = (
                'id', 'name', 'img', 'description', 'price',
                'language', 'no_of_page', 'year_of_publication',
                'total_number_of_book', 'author', 'category_name', 
                'publisher'
        )
        
    def get_category_name(self, obj):
        return obj.category.name

    def get_publisher(slef, obj):
        return obj.publisher.username

    