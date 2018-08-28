from django.db import models

# Create your models here.


class Deployment(models.Model):
    name = models.CharField(max_length=100, null=False)
    namespace = models.CharField(max_length=100, null=False, default="default")
    desired = models.IntegerField(null=True)
    unavailable = models.IntegerField(null=True)
    available = models.IntegerField(null=True)
    updated = models.IntegerField(null=True)
    svc_version = models.CharField(max_length=50, null=True)
