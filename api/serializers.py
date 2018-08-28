from rest_framework import serializers
from deployment.models import Deployment


class DeploymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deployment
        fields = ('id', 'name', 'namespace', 'available', 'desired', 'svc_version', 'unavailable', 'updated')