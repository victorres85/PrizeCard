from rest_framework import serializers
from .models import AppUserProfile, MyCards, MyCardsHistory
from django.contrib.auth.models import User
from django_countries.serializers import CountryFieldMixin


class RewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyCards
        fields = ('code',)


class UpdateMyCardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyCards
        fields = ('profile', 'card', 'points', 'created', 'updated', 'image')


class MyCardsSerializer(serializers.ModelSerializer):
    card = serializers.CharField(source='card.business.business_name')
    class Meta:
        model = MyCards
        fields = ('profile', 'card', 'points', 'created', 'updated', 'code', 'image')


class MyCardsHistorySerializer(serializers.ModelSerializer):
    card = serializers.CharField(source='card.business.business_name')

    class Meta:
        model = MyCardsHistory
        fields = ('profile', 'business', 'card', 'code', 'finalized')


class AppUserProfileSerializer(CountryFieldMixin, serializers.ModelSerializer):
    #myCards = serializers.SlugRelatedField(many=True, read_only=True, slug_field="card")

    class Meta:
        model = AppUserProfile
        fields = ('id', 'user','address_1', 'address_2', 'city', 'country',
        'post_code', 'phone_number', 'profile_picture', 'created', 'lat', 'long')#, 'myCards')

class ListUserSerializer(serializers.ModelSerializer):
    profile = AppUserProfileSerializer()
    class Meta:
        model = User
        fields = ('id','username', 'email', 'password', 'profile', )

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('id','username', 'email', 'password')

class MyCardCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyCards
        fields = ('code', )