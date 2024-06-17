from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from snippets.models import *
from snippets.serializer import *


# Create your views here.



class FruitsViewSet(viewsets.ModelViewSet):
    queryset = Fruits.objects.all()
    serializer_class = FruitsSerializer
    permission_classes = [AllowAny]






