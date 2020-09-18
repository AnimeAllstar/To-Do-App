from django.db import models
from django.contrib.auth.models import User

class TodoItem(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='item')
    #Date Created
    #Deadline
    #Categories (separate by comma)
    #title?
    #isFlagged
    #https://lh3.googleusercontent.com/defIipZiAF5d1UYgOmxrb-0CJ3-8XojdI0nZ6O9Z2DBq8GLHgFq7iph8M2Xw78FTgHE=w1536-h674-rw


#Make a TodoList Model - See microsoft To DO List app