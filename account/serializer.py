from rest_framework import serializers
from .models import Author, Publisher
from rest_framework.validators import UniqueValidator

#^ ----------------------------------------------  Author Serializer -----------------------------------------       
class AuthorSerializer(serializers.ModelSerializer):
    """Serialize author attributes to return when
        the end point is called"""

    class Meta:
        model = Author
        fields = '__all__'
 
#^ ----------------------------------------------  Publisher Serializer -----------------------------------------       
class PublisherSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Publisher
        fields = '__all__'
        