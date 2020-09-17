from django.db import models
from django.contrib.auth.models import User

class TodoItem(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='item')
