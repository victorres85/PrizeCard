from django.urls import path
from . import views

app_name = 'Business'

urlpatterns = [
    path('business', views.Teste ),
]