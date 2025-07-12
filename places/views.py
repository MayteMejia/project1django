from django.shortcuts import render
from django. http import HttpResponse, JsonResponse
from rest_framework import viewsets, generics
from rest_framework.decorators import api_view
from .models import Type, Ubication, Place
from .serializers import TypeSerializer, UbicationSerializer, PlaceSerializer

def index(request):
    return HttpResponse("Hello, world!")

class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

class TypeCreateView(generics.CreateAPIView, generics.ListAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

@api_view(['GET'])
def type_count(request):
    try:
        count = Type.objects.count()
        return JsonResponse({
            'count': count
        },
        safe=False,
        status=200,
        )
    except Exception as e:
        return JsonResponse({"message": str(e)}, status=400)

class UbicationViewSet(viewsets.ModelViewSet):
    queryset = Ubication.objects.all()
    serializer_class = UbicationSerializer

class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

@api_view(['GET'])
def place_by_priority(request):
    try:
        places = Place.objects.filter(priority='H')
        count = Place.objects.count()
        return JsonResponse(
            PlaceSerializer(places, many=True).data,
        safe=False,
        status=200,
        )
    except Exception as e:
        return JsonResponse({"message": str(e)}, status=400)