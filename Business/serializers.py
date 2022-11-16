from rest_framework import serializers
from .models import Businesses, Cards, Profile
from django.contrib.auth.models import User
import requests
from geopy.distance import great_circle


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}
    
class BusinessesSerializer(serializers.ModelSerializer):
    distance = serializers.SerializerMethodField('get_location')

    class Meta:
        model= Businesses
        fields = ('id', 'address_first_line', 'address_second_line',
                  'city', 'region', 'post_code', 'phone_number', 'logo', 'join_date', 'distance')

    def get_location(self, business):
        ip_info = requests.get('https://api64.ipify.org?format=json').json()
        ip_address = ip_info["ip"]
        response = requests.get(f'http://api.ipstack.com/{ip_address}?access_key=8eba29fcae0bbc63c1e93b8c370e4bcf').json() 
        location_data = {
            "ip": ip_address,
            "latitude": response.get("latitude"),
            "longitude": response.get("longitude")
        }
        latitude = response.get("latitude")
        longitude = response.get("longitude")
        first = (float(latitude), float(longitude))
        second = (business.lat, business.long)
        dist = great_circle(first, second).miles


        return dist


    


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Profile
        fields = ('user', 'phone_number', 'confirmation' )

class CardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cards
        fields = ('name', 'business', 'description', 'total_points')
