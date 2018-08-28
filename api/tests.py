from django.test import TestCase

# Create your tests here.
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import Http404, HttpResponse, JsonResponse
from coredb.models import kubernetes_db as db
from pprint import pprint
import json
# Create your views here.


def show_all_namespace_dep():
    deps = db.deployments.find()
    count = deps.count()
    pprint(count)
    deps_dict = {}
    deps_num = 0
    for i in deps:
        deps_num += 1
        deps_dict[str(deps_num)] = i
    print(deps_dict)


if __name__ == '__main__':
    show_all_namespace_dep()