# -*- coding:utf-8 -*-
from django.http import HttpResponse
from kubernetes import client, config
from kubernetes.client.rest import ApiException
from KubeManager import settings
from coredb.models import kubernetes_db
import re
# Create your views here.

pattern_version = re.compile('nexus\.sss\.com:18443/.*:(.*)$')
config.load_kube_config(settings.KUBERNETES_CONFIGFILE['test'])
instance_corev1 = client.CoreV1Api()
instance_appv1 = client.AppsV1Api()


def load_deployment_to_mongo(request):
    try:
        kubernetes_db.deployments.remove({})
        api_response = instance_appv1.list_deployment_for_all_namespaces(watch=False)
        for i in api_response.items:
            deployment = {}
            deployment['name'] = i.metadata.name
            deployment['namespace'] = i.metadata.namespace
            deployment['desired'] = i.status.replicas
            deployment['unavailable'] = i.status.unavailable_replicas
            deployment['updated'] = i.status.updated_replicas
            deployment['available'] = i.status.available_replicas
            containers = i.spec.template.spec.containers
            deployment['version'] = 'NULL'
            for j in containers:
                if j.name == 'java':
                    image = j.image
                    deployment['version'] = re.match(pattern_version, image).group(1)
            kubernetes_db.deployments.insert(deployment)
        return HttpResponse(r"Deployment数据被载入CoreDB中！")
    except ApiException as e:
        print("Exception when calling AppsV1Api->list_deployment_for_all_namespaces: %s\n" % e)
