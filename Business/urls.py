from django.urls import path, include
from . import viewset, views
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns



app_name = 'Business'

router = routers.SimpleRouter()
router.register(r'owner', viewset.ProfileViewSet, basename='profile_list')
router.register(r'business', viewset.BusinessesViewSet, basename='business_detail')
#router.register(r'user', viewset.UserViewSet, basename='user_list')
router.register(r'cards', viewset.CardsViewSet, basename='cards_detail')


urlpatterns = [
    path('', include(router.urls)),
 #   path(r'business/', views.BusinessesAPIView.as_view()),
 #   path(r'business/<int:pk>', views.BusinessesAPIView.as_view()),

   
]
