from rest_framework import serializers
from .models import CustomUser, CustomPublisher

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'first_name', 'last_name', 'password','phone','Profile_Pic')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user
    

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomPublisher
        fields = ('id', 'email', 'first_name', 'last_name', 'password', 'certificate')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        certificate = validated_data.pop('certificate', None)
        publisher = CustomPublisher.objects.create_user(**validated_data)
        publisher.certificate = certificate
        publisher.save()
        return publisher


class ChangeUserPasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)       
