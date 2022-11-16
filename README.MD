# Starting environment

To work with python we have first to create a virtual enviroment to hold our project, to do it you will navagate to the project directory on the terminal and run the following command (keep on mind the python3 and pip have to be previously installed):

`python -m venv env`

> Command used to create the virtual environment

`. env/bin/activate`

> Command used to activate our virtual env

`pip install -r requirements.txt`

> Command used to install all required libraries

`python manage.py runserver`

> This command will run the application, now if you enter the http://127.0.0.1:8000 you should see our application running on your browser

# CREATING NEW MODELS

To create our models we will be using the `models.py` file which is located inside our App_User directory, inside `models.py` make sure to have the following imports:

```python
from django.db import models
from django.contrib.auth.models import User
```

`models` will be used to extend the Model class into our tables class
`User` will be used for a OneToOneField relationship between our App_User model and the User model provided by Django.

Bellow you have an example of Model with some explanations:

```
Class Businesses(models.Model):
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

    def __unicode__(self):
        return self.user.username
```

`Class Businesses(models.Model):` -> creates our model called Business which extends models.Model (it's necessary to tell django to build a SQL table using the information we will declare insede this class)
`user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)`
`OneToOneField` -> creates a one to one relationshipe between Business and User Tables
`EmailField` -> creates a text field with predefine email validation, *max_length = 250* is a required parameter
`CharField` -> creates a text field with, *max_length = 200* is a required parameter
`IntegerField` -> creates a Integer Field
`ImageField` -> is a FileField with uploads restricted to image formats only, *upload_to=* is required, we will here pass the path for our image to be stored.
`DateTimeField` -> is used to work with date and time. *auto_now_add = True* will tell Django to automatically fill the field with the date and time of the moment of the object creation. (we could also use *auto_now=True,* this parameter is used to get the date and time field updated every time the object is modified.
`TextField` -> creates a text field that would accept multiple lines of text.

```
        def __unicode__(self):
        return self.user.username
```

> We are here defining the return from our class, so when we call it we receive the user username as return.
> to investigate which fields do we have on the user Model we can open the django shell on the terminal by writing
> `python3 manage.py shell`
> we can then import the user model with the code:
> `from django.contrib.auth.models import User`
> once the User model has been imported we can now run the command bellow and access all the properties from this model:
> `User.__dict__.keys()`

## AUTOMATICALLY CREATE A BUSINESS MODEL AFTER CREATING A USER MODEL

By using the method **receiver ** we can add a listener to our Business Model, so every time a user is created or modified a related business model will be also created or modified.

```Python
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_business_profile(sender, instance, created, **kwargs):
    if created:
        Businesses.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_business_profile(sender, instance, **kwargs):
    instance.businesses.save()
```

# CREATING SERIALIZER

To create the serializers we first have to import all the necessary models and also import serializer library from rest_framework.

We can then, follow the example below.

Create a Serializer by adding the name of the Model plus Serializer, we then extend the serializers.ModelSerializer and declare the Meta class.

inside the meta class we can add the model field which will be equal to the related Model and add fields where we will declare all fields we want to be visible on our Serializer .

* passing one serializer into another:

We can declare a variable linked to the target serializer and then use it as a field, we can see an example on BusinessesSerializer

```python
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username', 'first_name', 'last_name', 'email')


class BusinessesSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model= Businesses
        fields = ('user', 'address_first_line', 'address_second_line',
                  'city', 'region', 'post_code', 'phone_number', 'logo', 'join_date' )
```

# CREATING VIEWSETS

To create our views, we can have different approaches here we will be extending ModelViewSet class, which inherits from the GenericAPIView and implements a collection of different methods, such as: .list(), .retrieve(), .create(), .update(), .partial_update(), and .destroy()

here you have an exemple of implementation:

```Python
class AccountViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsAccountAdminOrReadOnly]
```

To learn more click thin [link](https://www.django-rest-framework.org/api-guide/viewsets/#modelviewset)


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

`celery -A PrizeCard.celery worker -l DEBUG -E`

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

## Adding extra field to BusinessSerializer

For this we will have to install a few packages: requests, ipify and geopy
`pip install requests ipify geopy`

Now on Serializers.py we will add the following imports:

```
import requests
from geopy.distance import great_circle
```

The updated BusinessesSerializer is found below with explanations below:

```python
class BusinessesSerializer(serializers.ModelSerializer):
    distance = serializers.SerializerMethodField('get_location')

    class Meta:
        model= Businesses
        fields = ('id', 'address_first_line', 'address_second_line',
                  'city', 'region', 'post_code', 'phone_number', 'logo', 'join_date', 'distance')

    def get_location(self, business):
        ip_info = requests.get('https://api64.ipify.org?format=json').json()
        ip_address = ip_info["ip"]
        response = requests.get(f'http://api.ipstack.com/{ip_address}?access_key=8eba29fcae0bbc63c1e93b8c370e4bcf').json() 
        latitude = response.get("latitude")
        longitude = response.get("longitude")
        first = (float(latitude), float(longitude))
        second = (business.lat, business.long)
        distance = great_circle(first, second).miles


        return distance
```

`distance = serializers.SerializerMethodField('get_location')`
The code above creates a variable called distance with the value which is returned by the **get_location** method, this variale will then be added to our fields list.

`def get_location(self, business):`
The function above is the one to be called by the SerializerMethodField which will pass a reference of each object to the **business** parameter

`ip_info = requests.get('https://api64.ipify.org?format=json').json()`
the line above will return the machine IP from the website api64 and will convert the information collected into json. we will then isolate the ip addres into the **ip_address** variable.

`response = requests.get(f'http://api.ipstack.com/{ip_address}?access_key=8eba29fcae0bbc63c1e93b8c370e4bcf').json()`
The line above will access the ipstack api, we will pass our ip\_address and the access\_key to return an json with different informations.

> IMPORTANT: ipstack is an api, which we have to pay, for now we are using the free_version which allow us to make 100 requisitions a month

we will then isolate the the latitude and longitude into different variables and pass it to a tuple called **first,** making sure each value is of Float Type.

`second = (business.lat, business.long)`

on the line above we are colecting the lat and long variables from each object on our model and passing it into a tupple named second

`distance = great_circle(first, second).miles`

finally here we are using the `great_circle` method from  **geopy.distance** to calculate the distance in miles from first and second locations

this variable is then returned to fill the information into the variable **distance  **which have been created at the beginning of our code and then passed to our **BusinessessSerializer FIELDS list**