from rest_framework import serializers
from .models import Author, Publisher
from rest_framework.validators import UniqueValidator

#jwt token imports
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


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


#^ ----------------------------------------------  JWTtoken obtain Serializer -----------------------------------------       
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims 
        token['email'] = user.email
        token['is_publisher'] = user.is_publisher
        token['is_staff'] = user.is_staff
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        # ...

        return token
