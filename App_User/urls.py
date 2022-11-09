from . import views
from django.urls import path


app_name = 'User'

urlpatterns = [
    path('user', views.Teste ),
]