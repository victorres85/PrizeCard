from django.shortcuts import render
from .serializers import BusinessesSerializer, CardsSerializer, UserSerializer
from .models import Businesses, Cards
from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet


# Create your views here.

class BusinessesViewSet(ModelViewSet):
    serializer_class = BusinessesSerializer
    queryset = Businesses.objects.all()


class CardsViewSet(ModelViewSet):
    serializer_class = CardsSerializer
    queryset = Cards.objects.all()  

class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()  