from django.db import models

class BayItem(models.Model):
    name = models.CharField(max_length = 50)
    default_img = models.CharField(max_length=250) #Image URL
    found_img = models.CharField(max_length=250) #Image URL
    gamers = models.ManyToManyField("Gamer", through="FoundItem", related_name='gamers_who_found_item')

    @property
    def found(self):
        return self.__found

    @found.setter
    def found(self, value):
        self.__found = value