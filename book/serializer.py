from rest_framework import serializers
from .models import Category, Book

class CategorySerializer(serializers.ModelSerializer):
    value = serializers.SerializerMethodField()
    label = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('value', 'label', 'slug')

    def get_value(self, obj):
        return obj.id
    
    def get_label(self, obj):
        return obj.name

        
class BookSerializer(serializers.ModelSerializer):
    
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), required=True)
    category_name = serializers.SerializerMethodField()
    author_name = serializers.SerializerMethodField()
    publisher = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = (
                'id', 'name', 'front_img', 'ISBN', 'back_img', 'description','author', 'author_name', 
                'category','category_name', 'price', 'language', 'no_of_page',
                'year_of_publication', 'total_number_of_book', 'publisher',
        )
        
    def get_category_name(self, obj):
        return obj.category.name

    def get_author_name(self, obj):
        return f'{obj.author.f_name} {obj.author.l_name}'
    
    def get_publisher(slef, obj):
        return f'{obj.publisher.first_name} {obj.publisher.last_name}'
    

    