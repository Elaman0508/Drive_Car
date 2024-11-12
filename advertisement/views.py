from rest_framework import generics
from .serializers import CarAdSerializer
from .models import CarAd
from rest_framework import viewsets




class CarAdListView(viewsets.ModelViewSet):
    queryset = CarAd.objects.all()
    serializer_class = CarAdSerializer



class CarAdCreateAPIView(generics.CreateAPIView):
    queryset = CarAd.objects.all()
    serializer_class = CarAdSerializer
