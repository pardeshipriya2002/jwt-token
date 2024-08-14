from .models import *
from rest_framework import serializers

class SchoolSerializers(serializers.ModelSerializer):
    class Meta:
        model=SchoolModel
        fields=["id","stu_name","stu_email","stu_roll"]

class StudentSerializers(serializers.ModelSerializer):
    class  Meta:
        model=StudentModel
        fields=["id","stu_name","stu_email","stu_roll"]     