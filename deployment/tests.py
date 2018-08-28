from django.test import TestCase

from deployment.models import Deployment

dep = Deployment.objects.create(
    name='test2',
    namespace='default',
    version='SNAPSHOT-0.0.1',
    desired=1,
    unavailable=1,
    updated=1,
    available=1
)
dep.save()