from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializer import UserSerializer, ListUserSerializer, RewardSerializer ,MyCardCodeSerializer, AppUserProfileSerializer, MyCardsSerializer, MyCardsHistorySerializer, UpdateMyCardsSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
import re
from .models import AppUserProfile, MyCards, MyCardsHistory
from PrizeCard.tasks import card_completed
import pytesseract
from PIL import Image
import random
from datetime import datetime
# Create your views here.

def CodeGenerator():
    nums = [random.randrange(1,9) for _ in range(6) ]
    code = ''.join(str(num) for num in nums)
    return code

    

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
    

    def get_serializer_class(self):
        if self.request.GET.get('code') != None:
            return RewardSerializer
        if self.action == 'update':
            return UpdateMyCardsSerializer
        else:
            return MyCardsSerializer

    def update(self, request, pk=None, *args, **kwargs):
        '''
        update the image, check if image contains the name of the business if so, increase the points by 1
        '''
        myCards_obj = MyCards.objects.get(id=pk)
        data = request.data
        myCards_obj.image = data["image"]
        myCards_obj.save()
        img = f"media/{myCards_obj.image}"
        result = pytesseract.image_to_string(img)
        business = myCards_obj.card.business.business_name
        total_points = myCards_obj.card.total_points
        date_pattern = "\d{2}[/-]\d{2}[/-]\d{4}"
        hour_pattern = "\d{2}[:]\d{2}[:]\d{2}"
        date = re.findall(date_pattern, result)
        hour = re.findall(hour_pattern, result)
        # validade image and add a point if everything is ok
        if 'Mezcale' in result:
            myCards_obj.points += 1
            # check if all the points have been acumulated, send an email with a congrats message and generates a code to be used by the custumer 
            if myCards_obj.points == 2:#  total_points:
                myCards_obj.points = 0
                card_completed.delay(myCards_obj.profile.user.pk)
                myCards_obj.code = CodeGenerator() 
                MyCardsHistory.objects.create(
                profile = myCards_obj.profile,
                card = myCards_obj.card,
                finalized = datetime.now(),
                code = myCards_obj.code,
                business = myCards_obj.card.business.business_name,
                )

        else:
            print(result)
            return Response("Please take a new picture")
             
        print(f'{str(date)}{str(hour)}')
        print(myCards_obj.profile.user.pk)
        myCards_obj.save()
        serializer = UpdateMyCardsSerializer(myCards_obj)
        return Response(serializer.data)
       


class MyCardsHistoryViewSet(ModelViewSet):
    serializer_class = MyCardsHistorySerializer
    queryset = MyCardsHistory.objects.all()