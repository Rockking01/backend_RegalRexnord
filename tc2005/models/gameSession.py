from django.db import models
from .user import User


class GameSession(models.Model):
    playerid = models.ForeignKey(User, on_delete=models.CASCADE)
    moduloJuego = models.IntegerField()
    nivel = models.IntegerField(null=True)
    velocidad = models.IntegerField()
    diferencia = models.IntegerField(null=True)
    errores = models.IntegerField(null=True)
    score = models.IntegerField()
    tiempoSesion = models.TimeField()
