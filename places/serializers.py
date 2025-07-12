from rest_framework import serializers
from .models import Type, Ubication, Place

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'

class UbicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ubication
        fields = '__all__'

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'