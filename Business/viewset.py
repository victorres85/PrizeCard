from django.shortcuts import render
from .serializers import BusinessesSerializer, CardsSerializer, UserSerializer, ProfileSerializer, ListBusinessesSerializer, PostUserSerializer
from .models import Businesses, Cards, Profile
from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from rest_framework.response import Response
import requests
from geopy.distance import great_circle


class BusinessesViewSet(ModelViewSet):
    serializer_class = BusinessesSerializer
    queryset = Businesses.objects.all()
    
    def list(self, request, pk=None):
        serializer_class = ListBusinessesSerializer

        #Get IP info once
        ip_info = requests.get('https://api64.ipify.org?format=json').json()
        ip_address = ip_info["ip"]
        response = requests.get(f'http://api.ipstack.com/{ip_address}?access_key=8eba29fcae0bbc63c1e93b8c370e4bcf').json()
        latitude = response.get("latitude")
        longitude = response.get("longitude")
        first = (float(latitude), float(longitude))

        # Calculate distances for all businesses and pass them as a context to our serializer
        businesses = Businesses.objects.all()
        distances = {}
        for business in businesses:
            second = (business.lat, business.long)
            distance = great_circle(first, second).miles
            distances[business.id] = distance
            
        # Sort by distance
        businesses_processed = ListBusinessesSerializer(businesses, many=True, context={'distances': distances}).data
        businesses_processed.sort(key=lambda x: x['distance'])


        return Response(businesses_processed)
        

class ProfileViewSet(ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

class CardsViewSet(ModelViewSet):
    serializer_class = CardsSerializer
    queryset = Cards.objects.all()  

class UserViewSet(ModelViewSet):
    def get_serializer_class(self):
        if self.action == 'list':
            return UserSerializer
        if self.action == 'create':
            return PostUserSerializer
        return UserSerializer # I dont' know what

    queryset = User.objects.all()  

