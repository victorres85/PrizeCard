from __future__ import absolute_import

from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth.models import User
from celery import shared_task
import datetime
#from App_User.models import MyCardsHistory
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

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

@shared_task()
def send_monthly_emails(*businesses):
    logger.info("The sample task just ran.")
    from Business.models import Businesses
    from App_User.models import MyCardsHistory
    from App_User.models import AppUserProfile
    current_month = datetime.date.today().month
    for business in businesses:
        try:
            business_id = Businesses.objects.filter(id=business).values('id')[0]['id']
            business_user_id = Businesses.objects.filter(id=business).values('user')[0]['user']
            business_user = list(User.objects.filter(id=business_user_id).values_list())
            business_email = business_user[0][7]
            myCards = MyCardsHistory.objects.filter(business=business_id, finalized__month=current_month-1).values()
            count = 0
            message_table = ''
            for card in myCards:
                count += 1
                profile_id = card['profile_id']
                code = card['code']
                finalized = str(card['finalized'])
                day = finalized[0:11] 
                person_id = AppUserProfile.objects.filter(id=profile_id).values()[0]['user_id'] 
                person_name = User.objects.filter(id = person_id).values()[0]['first_name']
                m = f'\n {person_name} - {code} - {day} '
                message_table+=m
            if count > 0:
                message_title= f"you have {count} prizeCards this month \n"        
                subject = f'Monthly PrizeCards report'
                message = message = message_title + message_table
                email = EmailMessage(subject, message, 'admin@myshop.com', (business_email, ))
                email.send()
        except:
            print(f"Business found : {business}")  


