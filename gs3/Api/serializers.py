from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
     name =serializers.CharField(max_length=100)
     roll =serializers.IntegerField()
     marks=serializers.IntegerField()

     def create(self, validated_data):
         return Student.objects.create(**validated_data)
    
     def update(self,instance,validated_data):
         print(instance.name)
         instance.name =validated_data.get('name',instance.name)   
         print(instance.name)
         instance.roll =validated_data.get('roll',instance.roll) 
         instance.marks =validated_data.get('marks',instance.marks) 
         instance.save()
         return instance