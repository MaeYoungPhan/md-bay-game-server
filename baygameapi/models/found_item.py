from django.db import models
from django.contrib.auth.models import User

class FoundItem(models.Model):
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE, related_name='gamer_found')
    bay_item = models.ForeignKey("BayItem", on_delete=models.SET_NULL, related_name='item_found', null=True)