from django.db import models

class Occasion(models.Model):
    name = models.CharField(max_length = 50)
    emoji = models.CharField(max_length = 1)
