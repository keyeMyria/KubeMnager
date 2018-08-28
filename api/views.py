# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import Http404, HttpResponse, JsonResponse
from coredb.models import kubernetes_db as db
import json
# Create your views here.


def index(request):
    return HttpResponse(u'欢迎访问“哭吧 API”')


def show_all_namespace_dep(request):
    deps = db.deployments.find({}, {'_id': 0})
    deps_dict = {}
    deps_num = 0
    for i in deps:
        deps_num += 1
        deps_dict[str(deps_num)] = i
    return JsonResponse(deps_dict)