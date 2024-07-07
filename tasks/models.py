from django.db import models

# Create your models here.
# tasks/models.py
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    STATUS_CHOICES = [
        ('Todo', 'Todo'),
        ('Inprogress', 'Inprogress'),
        ('Done', 'Done'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Todo')
    owner = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class TaskMember(models.Model):
    task = models.ForeignKey(Task, related_name='members', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.task.title}"
