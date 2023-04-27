from django.db import models

class BaySite(models.Model):
    name = models.CharField(max_length = 50)
    miles_to_oc = models.IntegerField()
    image = models.CharField(max_length=250)
    content = models.CharField(max_length=500)
    latitude = models.FloatField()
    longitude = models.FloatField()
