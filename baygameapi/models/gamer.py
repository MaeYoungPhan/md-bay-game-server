from django.db import models
from django.contrib.auth.models import User


class Gamer(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    found_items = models.ManyToManyField("BayItem", through="FoundItem", related_name='items_found_by_gamer')

    @property
    def found(self):
        return self.__found

    @found.setter
    def found(self, value):
        self.__found = value