from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify

# Create your models here.



class Businesses(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
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
            self.slug = slugify(self.user)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.slug


@receiver(post_save, sender=User)
def create_business_profile(sender, instance, created, **kwargs):
    if created:
        Businesses.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_business_profile(sender, instance, **kwargs):
    instance.businesses.save()


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