from rest_framework import serializers
from .models import Businesses, Cards, Profile
from django.contrib.auth.models import User


class CardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cards
        fields = ('name', 'business', 'description', 'total_points')


class ListBusinessesSerializer(serializers.ModelSerializer):
    distance = serializers.SerializerMethodField()

    class Meta:
        model= Businesses
        fields = ('id', 'business_name','address_first_line', 'address_second_line',
                  'city', 'region', 'post_code', 'phone_number', 'logo', 'join_date', 'distance')

    def get_distance(self, business):
        return self.context['distances'][business.id]

    
    
class BusinessesSerializer(serializers.ModelSerializer):
    cards = CardsSerializer(source='cards_set'   , many=True)

    class Meta:
        model= Businesses
        fields = ('id', 'address_first_line', 'address_second_line',
                  'city', 'region', 'post_code', 'phone_number', 'logo', 'join_date', 'cards') #'business_name', 
  
class ProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Profile
        fields = ('phone_number', 'confirmation' )


class UserSerializer(serializers.ModelSerializer):
    business =  BusinessesSerializer(source='businesses_set', many=True)
    profile =  ProfileSerializer()
    class Meta:
        model = User
        fields = ('id','username', 'email', 'password', 'profile','business')
        extra_kwargs = {'password': {'write_only': True}}

class PostUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username', 'email', 'password',)
        extra_kwargs = {'password': {'write_only': True}}


