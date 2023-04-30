from django.db import models
from .user import User


class Game(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    volumen = models.IntegerField(default=0)
   