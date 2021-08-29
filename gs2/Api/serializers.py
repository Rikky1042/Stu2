
from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.Serializer):
     name=serializers.CharField(max_length=100)
     roll=serializers.IntegerField()
     marks= serializers.IntegerField()

     def create(self, validate_data):
       return Student.objects.create(**validate_data)