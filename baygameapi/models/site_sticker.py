from django.db import models

class SiteSticker(models.Model):
    name = models.CharField(max_length = 50)
    default_img = models.CharField(max_length=250) #Image URL
    found_img = models.CharField(max_length=250) #Image URL
    bay_site = models.ForeignKey('BaySite', on_delete=models.DO_NOTHING)

    @property
    def found(self):
        return self.__found

    @found.setter
    def found(self, value):
        self.__found = value