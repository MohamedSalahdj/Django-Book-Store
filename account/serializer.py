from rest_framework import serializers
from .models import Author

class AuthorSerializer(serializers.ModelSerializer):
    """Serialize author attributes to return when
        the end point is called"""

    class Meta:
        model = Author
        fields = '__all__'
