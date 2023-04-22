# RESTful-API-Django

Modern web development relies heavily on APIs as they facilitate communication and data exchange between applications. Creating an API can be a daunting task, especially for those new to web development. However, with the help of Django and DjangoRestFramework, building robust and scalable APIs has become much easier.

Django is a Python-based web framework that provides a rich set of tools and libraries for developing web applications. On the other hand, DjangoRestFramework is a third-party library that extends Django's capabilities by adding support for creating RESTful APIs. This library offers a comprehensive set of tools and abstractions for building, testing, and deploying APIs, making it an invaluable resource for developers.

![image](https://user-images.githubusercontent.com/47337257/233770606-7be3ad0e-0d14-4ece-9cfe-24f59552205a.png)

## Steps:
### Setup
1. Create a virtual environment and activate your virtual environment
  ```
  python -m venv venv
  source ./venv/Scripts/activate
  ```
2. Install dependencies 
dj-database-url: A Django utility to configure database connections using environment variables or a Heroku-style database URL.
psycopg2-binary: A Python library that enables connecting and interacting with PostgreSQL databases, including executing SQL queries, managing transactions, and handling errors.
```
pip install django dj-database-url psycopg2-binary djangorestframework
```

3. Generate a new django project 
```
django-admin startproject travelproject
```
4. Test your dev server 
```
cd travelproject
python manage.py runserver
```
### Creating API
5. Create a new app 
```
django-admin startapp travels
```
6. In settings.py, install djangorestframework and the travels app
```
INSTALLED_APPS = [

    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'travels.apps.TravelsConfig',
    'rest_framework'
]
```

### Configuring Database
7. We will use dj-database-url. This package automatically detects the database URL from the DATABASE_URL environment variable.
To use it, let's import the package at the top of settings.py.
```
import dj_database_url
```
8. We will replace the default database configuration
```
DATABASES = {

    'default': dj_database_url.config(
        conn_max_age=600,
        conn_health_checks=True,
    ),
}
```

9. Lets use a Postgres database from bit.io, copy the connection details `postgresql://dbuser:dbpassword@db.bit.io/username/databasename`
Since we're not utilizing a .env file, we'll manually define the environmental variable in our terminal. Just remember that you'll need to define the variable again each time you open a new terminal. Here's an example of how to define the environmental variable for our bit.io Postgres database:
```
set DATABASE_URL=postgresql://dbuser:dbpassword@db.bit.io/username/databasename
```
To check if the DATABASE_URL was defined successfully, you can use the following command in your terminal:
echo %DATABASE_URL%


### Creating our Model
10. We will create a model called 'Travel' that can be used to store information about travel destinations, with fields for the destination name and details.
In the file travels/models.py, add a model
```
from django.db import models
class Travel(models.Model):
    destination = models.CharField(max_length=100)
    details = models.CharField(max_length=100)
```

11. Make and Run Migrations
```
python manage.py makemigrations
python manage.py migrate
```

12. Making Serializer
Django REST framework provides a convenient way to serialize model objects into JSON strings and deserialize them back into Python dictionaries. By building a serializer for our model with djangorestframework, we can handle this process seamlessly and also organize the data in a more conventional format.
```
from .models import Travel
from django.contrib.auth.models import User, Group
from rest_framework import serializers

# Our TravelSerializer
class TravelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # The model it will serialize
        model = Travel
        # the fields that should be included in the serialized output
        fields = ['id', 'destination', 'details']
```

### Creating Our Viewset
13. Django REST Framework provides ViewSets classes that enable us to conveniently establish all the necessary CRUD routes for our views.
In travels/views.py
```
from .models import Travel
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import TravelSerializer

class TravelViewSet(viewsets.ModelViewSet):

    ## The Main Query for the index route
    queryset = Travel.objects.all()

    # The serializer class for serializing output
    serializer_class = TravelSerializer

    # optional permission class set permission level
    permission_classes = [permissions.AllowAny] #Coule be [permissions.IsAuthenticated]
```
### Setting Up Our Router
14. To ensure that each of the methods in ViewSets is correctly mapped to its respective URLs, Django REST Framework includes a router that can handle this wiring.
We can now proceed to the urls.py file.
```
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from travels.views import TravelViewSet
from django.conf.urls import include

# create a new router
router = routers.DefaultRouter()

# register our viesets 
router.register(r'travels', TravelViewSet)

urlpatterns = [
    # add all of our router urls
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
```
### Testing the API with CRUD operation
* Run the project `python manage.py runserver`
* Use Postman to Create travel records with post requests to /travels/
* Get the full list with a get request to /travels/
* See one travel with a get request to /travels/<id>
* Edit a travel with a put request to /travels/<id>
* Delete a travel with delete request to /travels/<id>

![image](https://user-images.githubusercontent.com/47337257/233770517-9e551583-4834-4486-90ff-944d8880a926.png)


Reference:
https://www.linkedin.com/pulse/building-api-django-djangorestframework-ayelet-hillel/
