from django.db import models

class RecordOfTrip(models.Model):
    gamer = models.ForeignKey('Gamer', on_delete=models.CASCADE, related_name='gamer_id')
    date = models.DateField(auto_now=False, auto_now_add=False)
    name = models.CharField(max_length=55)
    occasion = models.ForeignKey('Occasion', on_delete=models.DO_NOTHING)
    number_found = models.IntegerField()

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        self.__author = value
