from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Businesses(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    email = models.EmailField(max_length = 250)
    address_first_line = models.CharField(max_length = 200)
    address_second_line = models.CharField(max_length = 200, blank=True)
    city = models.CharField(max_length = 100)
    region = models.CharField(max_length = 100)
    post_code = models.CharField(max_length = 10)
    phone_number = models.IntegerField()
    logo = models.ImageField(upload_to='media/businesses/%y/%m/%d', blank=True)
    join_date = models.DateTimeField(auto_now_add = True)
    active = models.BooleanField(default=True)

    def getNumberOfActiveBusinesses(self):
        return Businesses.objects.filter(active=True).count()

    def getNumberOfBusinesses(self):
        return Businesses.objects.all().count()

    def __unicode__(self):
        return self.user.username


class Cards(models.Model):
    name = models.CharField(max_length=200)
    business = models.ForeignKey(Businesses, on_delete=models.CASCADE)
    description = models.TextField()
    total_points = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, blank=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name