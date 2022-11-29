from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from Business.models import Cards
import random 
from PrizeCard.tasks import registration_completed
from geopy.geocoders import Nominatim
from Business.models import confirmation_code
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.template.defaultfilters import slugify
from datetime import datetime




# Create your models here.

class AppUserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, blank=True)
    address_1 = models.CharField(max_length=200, null=True, blank=True)
    address_2 = models.CharField(max_length=200, null=True, blank=True)
    post_code = models.CharField(max_length=10, null=True, blank=True)
    city = models.CharField(max_length=20, null=True, blank=True)
    country = CountryField(null=True, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='media/app_user/%y/%m/%d', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    lat = models.CharField(max_length=20, null=True, blank=True)
    long = models.CharField(max_length=20, null=True, blank=True)
    confirmation = models.CharField(max_length= 300, default=confirmation_code(), null=True)


    def save(self, *args, **kwargs):
        geolocator = Nominatim(user_agent="home")
        location = geolocator.geocode(self.post_code)
        self.lat = location.latitude
        self.long = location.longitude
        if not self.slug:
            self.slug = slugify(self.user.username)
       
        registration_completed.delay(self.user.pk, self.confirmation)

        return super().save(*args, **kwargs)

    def __str__(self):
        return self.slug

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        AppUserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.appuserprofile.save()


class MyCards(models.Model):
    profile = models.ForeignKey(AppUserProfile, on_delete=models.CASCADE)
    card = models.ForeignKey(Cards, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    
    def getNumberOfInitiatedCards(self):
        return MyCards.objects.filter(self.points>0).count()

 #   def update(self, *args, **kwargs):
 #       if self.points == self.card.total_points:
 #           print('CONGRATULATIONS YOU HAVE JUST COMPLETED YOUR CARD')
    
    def save(self, *args, **kwargs):
        if self.points == self.card.total_points:
            MyCardsHistory.objects.create(
                profile = self.profile,
                card = self.card,
                finalized = datetime.now()
            )
    

    def __str__(self):
        return self.card.business.business_name

class MyCardsHistory(models.Model):
    profile = models.ForeignKey(AppUserProfile, on_delete=models.CASCADE)
    card = models.ForeignKey(Cards, on_delete=models.CASCADE)
    finalized = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.profile.user.username} - {self.card.business.business_name}"
    