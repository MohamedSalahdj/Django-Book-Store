from rest_framework import generics,status, permissions
from .models import CustomUser, CustomPublisher
from .serializers import UserSerializer, PublisherSerializer,ChangeUserPasswordSerializer
from .models import CustomUser
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

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


class ChangeUserPassword(generics.UpdateAPIView):
    
    serializer_class = ChangeUserPasswordSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        user = self.request.user
        if not isinstance(user, CustomUser):
            raise NotFound("User not found.")
        return user

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        old_password = serializer.validated_data.get('old_password')
        new_password = serializer.validated_data.get('new_password')
        confirm_password = serializer.validated_data.get('confirm_password')

        if not self.object.check_password(old_password):
            raise ValidationError({"old_password": "Incorrect password."})

        if new_password != confirm_password:
            raise ValidationError({"confirm_password": "Passwords do not match."})

        self.object.set_password(new_password)
        self.object.save()

        return Response("Password changed successfully.", status=status.HTTP_200_OK)
    

class ListPublisherAPI(generics.ListAPIView):
    queryset = CustomPublisher.objects.all()
    serializer_class = PublisherSerializer
