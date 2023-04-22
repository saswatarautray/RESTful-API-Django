
# Making Our Serializer
#
# Django REST framework provides a convenient way to serialize model objects into JSON strings and deserialize them back into Python dictionaries.
# By building a serializer for our model with djangorestframework, we can handle this process seamlessly and also organize the data in a more conventional format.


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