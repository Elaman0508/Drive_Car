from rest_framework import serializers
from .models import *


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'price','title', 'body', 'engine', 'transmission', 'wheel', 'mileage', 'color', 'volume', 'states', 'descriptions', 'image']


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'price', 'title', 'body', 'engine', 'transmission', 'wheel', 'mileage', 'color', 'volume', 'states', 'descriptions', 'image']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'name', 'review', 'created_at']


class CharacteristicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Characteristic
        fields = ['id', 'brand', 'model', 'year_of_manufacture', 'price', 'image', 'views', 'comments_count']
