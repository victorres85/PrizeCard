# Asynchronous Tasks

## Workers, Message Queues, and Message Brokers

While your web server processes requests and returns responses, you need a second task-based server,
named worker, to process the asynchronous tasks. One or multiple workers can be running and executing
tasks in the background. These workers can access the database, process files, send e-mails, etc.
Workers can even queue future tasks. All while keeping the main web server free to process HTTP requests.

To tell the workers what tasks to execute we need to send messages. We communicate with brokers by
adding messages to a message queue, which is basically a first in, first out (FIFO) data structure.

## Sending email with Redis and Celery

On our application we will be using Redis as a Message broker and the Celery to manage our workers.

Redis (Remote Dictionary Server) is an in-memory data structure store, used as a distributed, in-memory key–value database, cache and message broker, with optional durability. Redis supports different kinds of abstract data structures, such as strings, lists, maps, sets, sorted sets, HyperLogLogs, bitmaps, streams, and spatial indices.

*Celery*, not only allow you to create asynchronous tasks easily and let them be executed by
workers as soon as possible, but you can also schedule them to run at a specific time.
https://docs.celeryq.dev/en/stable/index.html.

### Redis

To install and configure Redis we can follow the tutorial in the the following [link](https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-redis-on-ubuntu-18-04)
We also have to pip install it
`pip install redis`

### Celery

Let's start by pip installing Celery
`pip install celery`

Now we have to configure the celery on our **settings.py,**  by adding the following block of code:

```python
CELERY_BROKER_URL = 'redis://127.0.0.1:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Europe/London'
```

We then create a new file on the same directory where we have our settings.py, this new file will be called **celery.py **and should have the following information:

```python
import os
from celery import Celery
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PrizeCard.settings')

app = Celery('PrizeCard', broker_url='redis://127.0.0.1:6379')

app.conf.enable_utc = False
app.conf.update(timezone = 'Europe/London')

app.config_from_object(settings, namespace='CELERY')

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
```

Now on our app directory we will create the async tasks to be used, we then create a file called **tasks.py **and create our task, in his case we are creating a task to send a confirmation email, the code used is found below:

```python
from celery import shared_task
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth.models import User

@shared_task
def registration_completed(user_id, confirmation):
    user = User.objects.get(pk=user_id)
    subject = f'Welcome {user.username}, to PrizeCard'
    message = f'''Welcome to PrizeCard.
To confirm your email please use the code below
{confirmation}''' 
    email = EmailMessage(subject, message, 'admin@myshop.com', [user.email])
    email.send()
```

> Note that we have used the @shared_task notation, this is essential for celery to identify it as a task.

Finally we have to pass this task to the function we want to trigger it, in our case we will pass it to the save() method inside our Business models.

```python
def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user)
        registration_completed.delay(self.user.pk, self.confirmation)
        return super().save(*args, **kwargs)
```

> Note that we have used the keyword **delay **when calling our shared_task

As we are sending an email, we can not forget to configure our email server, for this we have to add the following to our **settings.py**

```python
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'victorres......@gmail.com'
EMAIL_HOST_PASSWORD = '{password}'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
```

Now that is all settle we can run our server and test our asynchronous function, we will need to run our celery/redis server separated of our project server, for this we need to run the code below in our terminal

`celery -A PrizeCard.celery worker -l DEBUG -E`

## Scheduling tasks

We have added a monthly task, which will be in charge to verify all the prizeCards that have been concluded during a period of time.

To schedule the time we have to add the following code to our settings.py, the code below will send an email every 1st of each month.

```Python
from celery.schedules import crontab
CELERY_BEAT_SCHEDULE = {
    'add-every-first-of-each-month':{
        'task':'PrizeCard.tasks.send_monthly_emails',
        'schedule': crontab(0, 0, day_of_month='1'),
        'args': ([x for x in range(100)])
    }
}
```

we also have to run the following command on the terminal: `celery -A PrizeCard.celery beat`

# GEOLOCALIZATION

We will divide this topic in two diferent parts:

First we will add the latitude and longitude to the Businesses model so we can have the exact location of each business, Second we will collect the ip address of the machine we are using and identified its location, it will be used to feed the BusinessesSerializer with a new field called **distance** which will be the calculation of the users IP location with each business location

## Adding latitude and longitude to the Businesses model

`geopy` is the library responsible for searching for the latitude and longitude. it will use the Nominatim api to retrieve those informations.

Let's start by installing it:
`pip install geopy`

Down here we have the code we have used inside models.py with explanations below it

```python
from django.db import models
from geopy.geocoders import Nominatim

class Businesses(models.Model):
    ...
    lat = models.CharField(max_length=20, null=True, blank=True)
    long = models.CharField(max_length=20, null=True, blank=True)

    def save(self, *args, **kwargs):
        geolocator = Nominatim(user_agent="Business")
        location = geolocator.geocode(self.post_code)
        self.lat = location.latitude
        self.long = location.longitude
        if not self.slug:
            self.slug = slugify(self.business_name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name
```

First we have imported the Nominatim library from geopy

`from geopy.geocoders import Nominatim`

We also have added 2 blank fields to our model:

`lat = models.CharField(max_length=20, null=True, blank=True)`

`long = models.CharField(max_length=20, null=True, blank=True)`

To fill those fildes with the required information we have overwrite the save method

`geolocator = Nominatim(user_agent="home")`

On `user_agent` we have to add our app's name.

`location = geolocator.geocode(self.pincode)`

By using the **geocode** method we can pass a pincode, a postcode or an address and have the latitude and longitude as return.

other option would be to use **reverse** where we would pass the latitude and longitude and have the address

`self.lat = location.latitude`

`self.long = location.longitude`

we will then assign the values of latitude and longitude to our model

## Calculating distance between business and user on viewset

For this we will have to install a few packages: requests, ipify and geopy
`pip install requests ipify geopy`

Now on viewser.py we will add the following imports:

```
import requests
from geopy.distance import great_circle
```

In order to calculate the distance between the business and the user we will overwrite the `list method` on our BusinessViewSet. Here we will iterate over each entry on our table adding a new field called 'distance' to it and before passing it to our serializer we still have to order our table by the new field in an ascending order.

Let's see our code here and get it analysed below.

```python
class BusinessesViewSet(ModelViewSet):
    serializer_class = BusinessesSerializer
    queryset = Businesses.objects.all()
    
    def list(self, request, pk=None):
        serializer_class = ListBusinessesSerializer

        #Get IP info once
        ip_info = requests.get('https://api64.ipify.org?format=json').json()
        ip_address = ip_info["ip"]
        response = requests.get(f'http://api.ipstack.com/{ip_address}?access_key=8eba29fcae0bbc63c1e93b8c370e4bcf').json()
        latitude = response.get("latitude")
        longitude = response.get("longitude")
        first = (float(latitude), float(longitude))

        # Calculate distances for all businesses and pass them as a context to our serializer
        businesses = Businesses.objects.all()
        distances = {}
        for business in businesses:
            second = (business.lat, business.long)
            distance = great_circle(first, second).miles
            distances[business.id] = distance
        
        # Sort by distance
        businesses_processed = BusinessesSerializer(businesses, many=True, context={'distances': distances}).data
        businesses_processed.sort(key=lambda x: x['distance'])


        return Response(businesses_processed)
```

first we get the IP address of the users, and asign it to a variable called **first****,** we then move to calculate the distance between the points.

the last thing to be done is to sort the resulting table using the new field 'distance' as parameter.

`ip_info = requests.get('https://api64.ipify.org?format=json').json()`
the line above will return the machine IP from the website api64 and will convert the information collected into json. we will then isolate the ip addres into the **ip_address** variable.

`response = requests.get(f'http://api.ipstack.com/{ip_address}?access_key=8eba29fcae0bbc63c1e93b8c370e4bcf').json()`
The line above will access the ipstack api, we will pass our ip_address and the access_key to return an json with different informations.

> IMPORTANT: ipstack is an api, which we have to pay, for now we are using the free_version which allow us to make 100 requisitions a month

we will then isolate the the latitude and longitude into different variables and pass it to a tuple called **first,** making sure each value is of Float Type.

`second = (business.lat, business.long)`

on the line above we are colecting the lat and long variables from each object on our model and passing it into a tupple named second

`distance = great_circle(first, second).miles`

finally here we are using the `great_circle` method from  **geopy.distance** to calculate the distance in miles from first and second locations

## Adding extra field to BusinessSerializer

To add the distance to our serializer, we first have to retrieve the

```python
class ListBusinessesSerializer(serializers.ModelSerializer):
    distance = serializers.SerializerMethodField()

    class Meta:
        model= Businesses
        fields = ('id', 'business_name','address_first_line', 'address_second_line',
                  'city', 'region', 'post_code', 'phone_number', 'logo', 'join_date', 'distance')

    def get_distance(self, business):
        return self.context['distances'][business.id]
```

`distance = serializers.SerializerMethodField()`
The code above creates a variable called distance with the value which is returned by the **get_location** method, this variable will then be added to our fields list.

`def get_location(self, business):`
The function above is the one to be called by the SerializerMethodField which will pass a reference of each object to the **business** parameter
