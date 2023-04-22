"""
URL configuration for travelproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]


# Setting Up Our Router
#
# To ensure that each of the methods in ViewSets is correctly mapped to its respective URLs, Django REST Framework includes a router that can handle this wiring.

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