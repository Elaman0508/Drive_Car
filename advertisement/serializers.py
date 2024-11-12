from rest_framework import serializers
from .models import CarAd



class CarAdSerializer(serializers.ModelSerializer):
    class Meta:
       model = CarAd
       fields = '__all__'

