from django.db import models

class RiverAndStream(models.Model):
    name = models.CharField(max_length = 50)
    miles_to_bay = models.DecimalField(max_digits=5, decimal_places=2)
    latitude = models.FloatField()
    longitude = models.FloatField()
    
    

