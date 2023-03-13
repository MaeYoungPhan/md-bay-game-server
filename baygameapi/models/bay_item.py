from django.db import models

class BayItem(models.Model):
    name = models.CharField(max_length = 50)
    default_img = models.CharField(max_length=250) #Image URL
    found_img = models.CharField(max_length=250) #Image URL
