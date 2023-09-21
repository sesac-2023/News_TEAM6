from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.exceptions import *
from rest_framework import status
from rest_framework import viewsets
from news6app.models import *
from news6app.serializers import *
import numpy as np


# Create your views here.

@api_view(['GET'])
def ListView(request):
    sql = 'select id from NEWS where (cat2_id between 20600 and 20699) or (cat2_id between 10400 and 10499) order by rand() limit 20'
    obj = News.objects.raw(sql)
    serializer = NewsSerializer(obj, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def NewsView(request, pk):
    sql = 'select id from NEWS where (cat2_id between 20600 and 20699) or (cat2_id between 10400 and 10499) order by rand() limit 20'
    obj = News.objects.raw(sql)
    serializer = NewsSerializer(obj, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def DetailView(request, pk):
    obj = News.objects.get(pk=pk)
    serializer = LatestNewsSerializer(obj)
    return Response(serializer.data)