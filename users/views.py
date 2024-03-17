from rest_framework import generics
from .models import CustomUser, CustomPublisher
from .serializers import UserSerializer, PublisherSerializer

class CreateUser(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class GetUsers(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class GetUser(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class UpdateUser(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class DeleteUser(generics.DestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class CreatePublisher(generics.CreateAPIView):
    queryset = CustomPublisher.objects.all()
    serializer_class = PublisherSerializer
