from django.db import models


class AuthRegistro(models.Model):
    ACTIVE = 'active'
    USED = 'used'
    SENDED = 'sended'
    STATUS_CHOICES = [
        (ACTIVE, 'Active'),
        (USED, 'Used'),
        (SENDED, 'Sended'),
    ]
    authKey = models.CharField(primary_key=True, max_length=10)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
