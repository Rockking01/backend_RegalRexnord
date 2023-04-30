from django.db import models
from .user import User

class Messages(models.Model):
    senderID = models.ForeignKey(User, on_delete=models.CASCADE )
    receiverID = models.ForeignKey(User, on_delete=models.CASCADE )
    text = models.TextField()