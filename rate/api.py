from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .models import *
from .serializers import *
# @api_view(['GET'])
# def allRates(req):
#     all_rates=Rate.objects.all()
#     data= RateSerializer(all_rates,many=True).data
#     return Response ({'data':data})


class ListAndCreateRates(generics.ListCreateAPIView):
    queryset=Rate.objects.all()
    serializer_class=RateSerializer


class GetRateById(generics.RetrieveAPIView):
    queryset=Rate.objects.all()
    serializer_class=RateSerializer
    lookup_field='id'

class DeleteRateById(generics.DestroyAPIView):
    queryset=Rate.objects.all()
    serializer_class=RateSerializer
    lookup_field='id'

class UpdateRateById(generics.UpdateAPIView):
    queryset=Rate.objects.all()
    serializer_class=RateSerializer
    lookup_field='id'

