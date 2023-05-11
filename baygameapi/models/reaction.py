from django.db import models

class Reaction(models.Model):
    name = models.CharField(max_length = 50)
    emoji = models.CharField(max_length = 1)
