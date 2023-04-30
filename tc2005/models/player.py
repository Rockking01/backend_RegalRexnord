from django.db import models
from .user import User


class Player(models.Model):
    UsuarioID = models.ForeignKey(User, on_delete=models.CASCADE)
    aggregateScore = models.IntegerField(default=0)