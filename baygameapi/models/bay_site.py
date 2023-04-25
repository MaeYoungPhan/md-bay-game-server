from django.db import models

class BaySite(models.Model):
    name = models.CharField(max_length = 50)
    miles_to_oc = models.IntegerField()
    image = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    latitude = models.FloatField()
    longitude = models.FloatField()

    @property
    def found(self):
        return self.__found

    @found.setter
    def found(self, value):
        self.__found = value