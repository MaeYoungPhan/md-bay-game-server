from django.db import models

class BaySiteItem(models.Model):
    name = models.CharField(max_length = 50)
    bay_site = models.ForeignKey('BaySite', on_delete=models.DO_NOTHING)
    description = models.CharField(max_length=500)
    default_img = models.CharField(max_length=250) #Image URL
    found_img = models.CharField(max_length=250) #Image URL


    @property
    def found(self):
        return self.__found

    @found.setter
    def found(self, value):
        self.__found = value