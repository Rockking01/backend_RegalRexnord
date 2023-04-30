from django.db import models
from .player import Player


class GameSession(models.Model):
    playerid = models.ForeignKey(Player, on_delete=models.CASCADE)
    moduloJuego = models.IntegerField()
    nivel = models.IntegerField(null=True)
    velocidad = models.IntegerField()
    diferencia = models.IntegerField(null=True)
    errores = models.IntegerField(null=True)
    score = models.IntegerField()
    tiempoSesion = models.TimeField()
