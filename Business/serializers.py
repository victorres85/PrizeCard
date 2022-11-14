from rest_framework import serializers
from .models import Businesses, Cards
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username', 'first_name', 'last_name', 'email')


class BusinessesSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model= Businesses
        fields = ('user', 'address_first_line', 'address_second_line',
                  'city', 'region', 'post_code', 'phone_number', 'logo', 'join_date' )



class CardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cards
        fields = ('name', 'business', 'description', 'total_points')
