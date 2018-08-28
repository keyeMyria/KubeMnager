from django.contrib import admin
from django.urls import path, include, reverse
from .views import *
urlpatterns = [
    path('load/', load_deployment_to_mongo, name="load"),
]