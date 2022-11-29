from django.urls import path, include
from . import viewset
from rest_framework import routers



app_name = 'App_User'

router = routers.SimpleRouter()
router.register(r'user', viewset.UserViewSet, basename='appUserProfile_list')
router.register(r'mycards', viewset.MyCardsViewSet, basename='myCards_list')
router.register(r'mycardshistory', viewset.MyCardsHistoryViewSet, basename='myCardsHistory_list')


urlpatterns = [
    path('', include(router.urls)),   
]
