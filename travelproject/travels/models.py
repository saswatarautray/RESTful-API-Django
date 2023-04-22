from django.db import models

# We will create one model called 'Travel' that can be used to store information about travel destinations,
# with fields for the destination name and details.
class Travel(models.Model):
    destination = models.CharField(max_length=100)
    details = models.CharField(max_length=100)


# Make and Run Migrations
#
# python manage.py makemigrations
#
# python manage.py migrate

