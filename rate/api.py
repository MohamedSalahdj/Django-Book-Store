from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .models import *
from rest_framework import permissions
from .serializers import *
from rest_framework.permissions import IsAuthenticated
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
    # permission_classes = [IsAuthenticated]  -->Uncomment for authentication
    # permission_classes = (CustomPermission,)


class GetRateById(generics.RetrieveAPIView):
    queryset=Rate.objects.all()
    serializer_class=RateSerializer
    lookup_field='id'


class DeleteRateById(generics.DestroyAPIView):
    queryset=Rate.objects.all()
    serializer_class=RateSerializer
    lookup_field='id'
    # permission_classes = [IsAuthenticated] -->Uncomment for authentication
    # permission_classes = (CustomPermission,)


class UpdateRateById(generics.UpdateAPIView):
    queryset=Rate.objects.all()
    serializer_class=RateSerializer
    lookup_field='id'
    # permission_classes = [IsAuthenticated]   -->Uncomment for authentication
    # permission_classes = (CustomPermission,)

@api_view(['GET'])
def allBookRates(req,id):
    all_rates=Rate.objects.all()
    data= RateSerializer(Rate.GetBookRates(id),many=True).data
    return Response ({'data':data})