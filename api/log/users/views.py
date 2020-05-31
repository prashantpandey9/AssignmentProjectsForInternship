from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets 
from .models import *
from .serializers import *

class PostView(viewsets.ModelViewSet):
	queryset=Post.objects.all()
	serializer_class=postSerializer