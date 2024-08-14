from django.shortcuts import render

# Create your views here.

from rest_framework.permissions  import IsAuthenticated,IsAdminUser
from .models import*
from .serializers import SchoolSerializers, StudentSerializers
from rest_framework import viewsets
from rest_framework.authtoken.models import Token

class SchoolViewSet(viewsets.ModelViewSet):
    permission_classes =[IsAdminUser]
    queryset =SchoolModel.objects.all()
    serializer_class = SchoolSerializers


class StudentViewSet(viewsets.ModelViewSet):
    permission_classes =[IsAuthenticated]
    queryset =SchoolModel.objects.all()
    serializer_class = SchoolSerializers

