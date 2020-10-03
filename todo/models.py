from django.db import models
import datetime
from django.contrib.auth.models import User


class TodoList(models.Model):
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='todo_list')
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100, blank=True, null=True)
    # color - list of options

    def __str__(self):
        return self.title


class TodoItem(models.Model):
    itemOf = models.ForeignKey(
        TodoList, on_delete=models.CASCADE, related_name='todo_item')
    content = models.CharField(max_length=100)
    isFlagged = models.BooleanField(default=False)
    isCompleted = models.BooleanField(default=False)
    deadline = models.DateField()

    def __str__(self):
        return self.content

    class Meta:
        ordering = ['deadline']  # ['-deadline'] for descending
