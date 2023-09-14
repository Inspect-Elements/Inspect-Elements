from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
# Create your views here.
from rest_framework import viewsets
from .serializers import ImageSerializer


# https://blog.devgenius.io/viewset-and-modelviewset-in-drf-690ab99a7afa
class ImageCreateView(viewsets.ModelViewSet):
    pass