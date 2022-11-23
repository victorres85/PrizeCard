from rest_framework import serializers
from .models import Businesses, Cards, Profile
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}
    
class PostBusinessesSerializer(serializers.ModelSerializer):

    class Meta:
        model= Businesses
        fields = ('id', 'address_first_line', 'address_second_line',
                  'city', 'region', 'post_code', 'phone_number', 'logo', 'join_date') #'business_name', 


class BusinessesSerializer(serializers.ModelSerializer):
    distance = serializers.SerializerMethodField()

    class Meta:
        model= Businesses
        fields = ('id', 'business_name','address_first_line', 'address_second_line',
                  'city', 'region', 'post_code', 'phone_number', 'logo', 'join_date', 'distance')

      # Get distance by business id from context we passed from our APIView
    def get_distance(self, business):
        return self.context['distances'][business.id]

    # def get_location(self, business):
    #     ip_info = requests.get('https://api64.ipify.org?format=json').json()
    #     ip_address = ip_info["ip"]
    #     response = requests.get(f'http://api.ipstack.com/{ip_address}?access_key=8eba29fcae0bbc63c1e93b8c370e4bcf').json() 
    #     latitude = response.get("latitude")
    #     longitude = response.get("longitude")
    #     first = (float(latitude), float(longitude))
    #     second = (business.lat, business.long)
    #     distance = great_circle(first, second).miles

    #     return distance

    

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Profile
        fields = ('user', 'phone_number', 'confirmation' )

class CardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cards
        fields = ('name', 'business', 'description', 'total_points')
