from django.contrib import admin
from .models import Businesses, Cards
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


 

# class BusinessesInline(admin.StackedInline):
#     model = Businesses
#     can_delete = False
#     verbose_name_plural = 'Business'
#     fk_name = 'user'

# class CustomBusinessAdmin(UserAdmin):
#     inlines = (BusinessesInline, )

#     def get_inline_instances(self, request, obj=None):
#         if not obj:
#             return list()
#         return super(CustomBusinessAdmin, self).get_inline_instances(request, obj)

admin.site.register(Businesses)
admin.site.register(Cards)

# Register your models here.
