from __future__ import absolute_import

from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth.models import User
from celery import shared_task

@shared_task(queue='celery', name='registration_completed')
def registration_completed(user_id, confirmation):
    user = User.objects.get(pk=user_id)
    subject = f'Welcome {user.username}, to PrizeCard'
    message = f'''Welcome to PrizeCard.
To confirm your email please use the code below
{confirmation}''' 
    email = EmailMessage(subject, message, 'admin@myshop.com', [user.email])
    email.send()

@shared_task(queue='celery', name='card_completed')
def card_completed(user_id):
    user = User.objects.get(pk=user_id)
    subject = f'Welcome {user.username}, to PrizeCard'
    message = f'''Congratulations, you have just completed your card''' 
    email = EmailMessage(subject, message, 'admin@myshop.com', [user.email])
    email.send()



