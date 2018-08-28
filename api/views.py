# -*- coding: utf-8 -*-
from deployment.models import Deployment
from api.serializers import DeploymentSerializer
from rest_framework import mixins
from rest_framework import generics
from django.http import Http404,HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


def index(request):
    return HttpResponse(u'欢迎访问“哭吧 API”')


class DeploymentList(APIView):

    def get(self, request):
        deployments = Deployment.objects.all()
        serializer = DeploymentSerializer(deployments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DeploymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeploymentDetail(APIView):

    def get_object(self, name):
        try:
            return Deployment.objects.get(name=name)
        except Deployment.DoesNotExist:
            raise Http404

    def get(self, request, name):
        deployments = self.get_object(name)
        serializer = DeploymentSerializer(deployments)
        return Response(serializer.data)

    def put(self, request, name):
        deployments = self.get_object(name)
        serializer = DeploymentSerializer(deployments, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, name):
        deployments = self.get_object(name)
        deployments.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


