# tasks/urls.py
from django.urls import path
from .views import (
    RegisterUserAPIView, CustomAuthToken, TaskCreateView, TaskListView, TaskDetailView, 
    TaskUpdateView, TaskDeleteView, TaskMemberAddView, TaskMemberRemoveView, TaskMemberListView
)

urlpatterns = [
    path('register/', RegisterUserAPIView.as_view(), name='register'),
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/create/', TaskCreateView.as_view(), name='task-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('tasks/<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
    path('tasks/<int:pk>/members/', TaskMemberListView.as_view(), name='task-member-list'),
    path('tasks/<int:pk>/members/add/', TaskMemberAddView.as_view(), name='task-member-add'),
    path('tasks/members/<int:pk>/remove/', TaskMemberRemoveView.as_view(), name='task-member-remove'),
]
