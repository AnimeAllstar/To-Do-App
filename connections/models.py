from django.db import models
from django.contrib.auth.models import User


class Connection(models.Model):
    creator = models.ForeignKey(
        User, related_name="connection_creator", on_delete=models.CASCADE)
    connections = models.ManyToManyField(User)

    def __str__(self):
        return self.creator.username

    @classmethod
    def add_connection(cls, creator_user, connect_user):
        friend = cls.objects.get_or_create(creator_user=creator_user)
        friend.connections.add(connect_user)

    @classmethod
    def remove_connection(cls, creator_user, connect_user):
        friend = cls.objects.get_or_create(creator=creator_user)
        friend.connections.remove(connect_user)
