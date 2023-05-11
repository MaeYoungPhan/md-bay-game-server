from django.db import models
from django.contrib.auth.models import User

class GamerAvatar(models.Model):
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE, related_name='gamer_pic')
    avatar = models.ForeignKey("Avatar", on_delete=models.SET_NULL, related_name='avatar_chosen', null=True)
