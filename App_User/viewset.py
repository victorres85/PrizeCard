from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializer import UserSerializer, ListUserSerializer, AppUserProfileSerializer, MyCardsSerializer, MyCardsHistorySerializer
from django.contrib.auth.models import User

from .models import AppUserProfile, MyCards, MyCardsHistory

# Create your views here.

class UserViewSet(ModelViewSet):
    def get_serializer_class(self):
        if self.action == 'list':
            return ListUserSerializer
        if self.action == 'create':
            return UserSerializer
        return UserSerializer # I dont' know what

    queryset = User.objects.all()



class AppUserProfileViewSet(ModelViewSet):
    serializer_class = AppUserProfileSerializer
    queryset = AppUserProfile.objects.all()



class MyCardsViewSet(ModelViewSet):
    serializer_class = MyCardsSerializer
    queryset = MyCards.objects.all()


class MyCardsHistoryViewSet(ModelViewSet):
    serializer_class = MyCardsHistorySerializer
    queryset = MyCardsHistory.objects.all()