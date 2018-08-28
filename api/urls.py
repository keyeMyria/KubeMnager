from django.contrib import admin
from django.urls import path, include, reverse
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('v1/', index, name="index"),
    path('v1/deployments/', DeploymentList.as_view()),
    path('v1/deployments/<str:name>/', DeploymentDetail.as_view()),
]