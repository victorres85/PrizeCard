from django.urls import path, include
from . import viewset
from rest_framework import routers


app_name = 'Business'

router = routers.SimpleRouter()
router.register(r'profile', viewset.ProfileViewSet, basename='profile_list')
router.register(r'business', viewset.BusinessesViewSet, basename='business_list')
router.register(r'user', viewset.UserViewSet, basename='user_list')
router.register(r'cards', viewset.CardsViewSet, basename='cards_detail')


urlpatterns = [
    path('', include(router.urls)),
   
]