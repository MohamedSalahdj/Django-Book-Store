from rest_framework import generics
from .models import Publisher
from .serializer import PublisherSerializer

class PublisherListApi(generics.ListAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

class PublisherDetailsApi(generics.RetrieveAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    
class PublisherCreateApi(generics.CreateAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    
class  PublisherUpdateApi(generics.RetrieveUpdateAPIView):
    queryset =  Publisher.objects.all()
    serializer_class =  PublisherSerializer
    
class PublisherDeleteApi(generics.DestroyAPIView):
    queryset = Publisher.objects.all()