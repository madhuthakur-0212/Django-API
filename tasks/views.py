from django.shortcuts import render

# Create your views here.
# tasks/views.py
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth.models import User
from .models import Task, TaskMember
from .serializers import UserSerializer, TaskSerializer, TaskMemberSerializer
# User Registration View
class RegisterUserAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            response_data = {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'message': 'User registered successfully.'
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            errors = serializer.errors
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

# Task Views
class TaskCreateView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class TaskListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

class TaskDetailView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

class TaskUpdateView(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

class TaskDeleteView(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

# Task Member Views
class TaskMemberAddView(generics.CreateAPIView):
    queryset = TaskMember.objects.all()
    serializer_class = TaskMemberSerializer
    permission_classes = [IsAuthenticated]

class TaskMemberRemoveView(generics.DestroyAPIView):
    queryset = TaskMember.objects.all()
    serializer_class = TaskMemberSerializer
    permission_classes = [IsAuthenticated]

class TaskMemberListView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        task_id = self.kwargs['pk']
        task = Task.objects.get(id=task_id)
        members = task.members.all()
        return User.objects.filter(taskmember__in=members)

# Custom Login View
class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user': UserSerializer(user).data
        })