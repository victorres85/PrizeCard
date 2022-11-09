from django.urls import path, include
from . import viewset
from rest_framework import routers


app_name = 'Business'

router = routers.SimpleRouter()
router.register(r'business', viewset.BusinessesViewSet, basename='business_detail')
router.register(r'cards', viewset.CardsViewSet, basename='cards_detail')


urlpatterns = [
    path('', include(router.urls)),
]