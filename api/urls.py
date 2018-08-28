from django.contrib import admin
from django.urls import path, include, reverse
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('v1/', index, name="index"),
    path('v1/deployments/', show_all_namespace_dep, name="show_all_namespace_dep")
]