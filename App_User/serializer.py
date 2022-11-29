from rest_framework import serializers
from .models import AppUserProfile, MyCards, MyCardsHistory
from django.contrib.auth.models import User
from django_countries.serializers import CountryFieldMixin



class MyCardsSerializer(serializers.ModelSerializer):
    card = serializers.CharField(source='card.business.business_name')
   # profile = serializers.CharField(source='profile.user.first_name')

    class Meta:
        model = MyCards
        fields = ('profile', 'card', 'points', 'created', 'updated')


class MyCardsHistorySerializer(serializers.ModelSerializer):
    card = serializers.CharField(source='card.business.business_name')

    class Meta:
        model = MyCardsHistory
        fields = ('profile', 'card', 'finalized')


class AppUserProfileSerializer(CountryFieldMixin, serializers.ModelSerializer):
    print(AppUserProfile.__dict__.keys())
    myCards = serializers.SlugRelatedField(many=True, read_only=True, slug_field="card")

     #MyCardsSerializer(source='mycards_set', many=True)
    class Meta:
        model = AppUserProfile
        fields = ('id', 'user','address_1', 'address_2', 'city', 'country',
        'post_code', 'phone_number', 'profile_picture', 'created', 'lat', 'long', 'myCards')

class ListUserSerializer(serializers.ModelSerializer):
    profile = AppUserProfileSerializer()
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'profile', )

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password')