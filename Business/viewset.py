from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import BusinessesSerializer, CardsSerializer

from .models import Businesses, Cards
# Create your views here.

class BusinessesViewSet(ModelViewSet):
    serializer_class = BusinessesSerializer

    def get_queryset(self):
        return Businesses.objects.all().order_by("id")
    
class CardsViewSet(ModelViewSet):
    serializer_class = CardsSerializer

    def get_queryset(self):
        return Cards.objects.all().order_by("id")