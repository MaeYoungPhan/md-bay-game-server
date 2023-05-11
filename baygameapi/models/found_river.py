from django.db import models
from django.contrib.auth.models import User

class FoundRiver(models.Model):
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE, related_name='gamer_water')
    water = models.ForeignKey("RiverAndStream", on_delete=models.SET_NULL, related_name='water_found', null=True)
