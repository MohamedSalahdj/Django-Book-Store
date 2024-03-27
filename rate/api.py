from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .models import *
from rest_framework import permissions
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from rest_framework import status

# @api_view(['GET'])
# def allRates(req):
#     all_rates=Rate.objects.all()
#     data= RateSerializer(all_rates,many=True).data
#     return Response ({'data':data})

from rest_framework import permissions

# class CustomPermission(permissions.BasePermission):
#     def has_permission(self, request, view):
#         if view.action in ('update', 'destroy','create'):
#             return request.user.is_authenticated
#         return True


class ListRates(generics.ListAPIView):
    queryset=Rate.objects.all()
    serializer_class=RateSerializer



class CreateRates(generics.CreateAPIView):
    queryset=Rate.objects.all()
    serializer_class=RateSerializer
    permission_classes = [IsAuthenticated] 

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class GetRateById(generics.RetrieveAPIView):
    queryset=Rate.objects.all()
    serializer_class=RateSerializer
    permission_classes = [IsAuthenticated]
    lookup_field='id'
    


class DeleteRateById(generics.DestroyAPIView):
    queryset=Rate.objects.all()
    serializer_class=RateSerializer
    lookup_field='id'
    permission_classes = [IsAuthenticated] 

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if(request.user!=instance.user):
            raise ValidationError('only review owner can delete his review')
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    # -->Uncomment for authentication
    # permission_classes = (CustomPermission,)


class UpdateRateById(generics.UpdateAPIView):
    queryset=Rate.objects.all()
    serializer_class=RateSerializer
    lookup_field='id'
    permission_classes = [IsAuthenticated] 


    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        if(request.user!=instance.user):
            raise ValidationError('only review owner can update his review')
        self.perform_update(serializer)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    #  -->Uncomment for authentication
    # permission_classes = (CustomPermission,)

@api_view(['GET'])
def allBookRates(req,id):
    all_rates=Rate.objects.filter(book=id)
    data= RateSerializer(all_rates,many=True).data
    return Response ({'data':data})