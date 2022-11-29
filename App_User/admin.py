from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.AppUserProfile)
admin.site.register(models.MyCards)
admin.site.register(models.MyCardsHistory)
