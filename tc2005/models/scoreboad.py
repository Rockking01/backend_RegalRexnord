from django.db import models
from .user import User


class Scoreboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    score = models.IntegerField(default=0)
   