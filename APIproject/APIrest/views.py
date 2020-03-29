from django.shortcuts import render
from rest_framework import viewsets
from .models import PGLlist
from .serializers import PgllistSerializer

# Create your views here.

class PgllistViewset(viewsets.ModelViewSet):
    serializer_class = PgllistSerializer
    queryset = PGLlist.objects.all()