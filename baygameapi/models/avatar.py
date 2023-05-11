from django.db import models

class Avatar(models.Model):
    name = models.CharField(max_length = 50)
    image = models.CharField(max_length=250)
