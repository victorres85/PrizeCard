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

`Class Businesses(models.Model):` -\> creates our model called Business which extends models.Model (it's necessary to tell django to build a SQL table using the information we will declare insede this class)
`user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)`
`OneToOneField` -\> creates a one to one relationshipe between Business and User Tables
`EmailField` -\> creates a text field with predefine email validation, *max_length = 250* is a required parameter
`CharField` -\> creates a text field with, *max_length = 200* is a required parameter
`IntegerField` -\> creates a Integer Field
`ImageField` -\> is a FileField with uploads restricted to image formats only, *upload_to=* is required, we will here pass the path for our image to be stored.
`DateTimeField` -\> is used to work with date and time. *auto\_now\_add = True* will tell Django to automatically fill the field with the date and time of the moment of the object creation. (we could also use *auto_now=True,* this parameter is used to get the date and time field updated every time the object is modified.
`TextField` -\> creates a text field that would accept multiple lines of text.

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