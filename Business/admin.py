from django.contrib import admin
from .models import Businesses, Cards
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

admin.site.register(Businesses)
admin.site.register(Cards)

