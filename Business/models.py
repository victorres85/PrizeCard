from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
import random 
from .tasks import registration_completed

# Create your models here.

def confirmation_code():
    code = ''
    for i in range(15):
        x = random.randint(34,91)
        if i%2 == 0:
            x = chr(x)
        code += str(x)
    return code     

class Profile(models.Model):
    confirmation = models.CharField(max_length= 300, default=confirmation_code(), null=True)
    phone_number = models.IntegerField(null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    slug = models.SlugField(max_length=200, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        registration_completed.delay(self.user.pk, self.confirmation)
        return super().save(*args, **kwargs)

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()



class Businesses(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    slug = models.SlugField(blank=True, unique=True)
    business_name = models.CharField(max_length = 200, blank=True)
    address_first_line = models.CharField(max_length = 200, blank=True)
    address_second_line = models.CharField(max_length = 200, blank=True)
    city = models.CharField(max_length = 100, blank=True) 
    region = models.CharField(max_length = 100,blank=True)
    post_code = models.CharField(max_length = 10, blank=True)
    phone_number = models.IntegerField(null=True)
    logo = models.ImageField(upload_to='media/businesses/%y/%m/%d', blank=True)
    join_date = models.DateTimeField(auto_now_add = True)
    active = models.BooleanField(default=True, blank=True)
   

    def getNumberOfActiveBusinesses(self):
        return Businesses.objects.filter(active=True).count()

    def getNumberOfBusinesses(self):
        return Businesses.objects.all().count()

    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.business_name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.slug




class Cards(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    business = models.ForeignKey(Businesses, on_delete=models.CASCADE)
    description = models.TextField()
    total_points = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, blank=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name