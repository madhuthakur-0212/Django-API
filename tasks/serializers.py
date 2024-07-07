# tasks/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task, TaskMember

class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'due_date', 'status', 'owner']

class TaskMemberSerializer(serializers.ModelSerializer):
    class Meta: 
        model = TaskMember
        fields = ['id', 'task', 'user']

class UserSerializer(serializers.ModelSerializer):
     class Meta:
         model = User
         fields = ['email', 'username', 'password']
         extra_kwargs = {'password': {'write_only': True}}

     def create(self, validated_data):
         user = User(
             email=validated_data['email'],
             username=validated_data['username']
         )
         user.set_password(validated_data['password'])
         user.save()
         return user

        
