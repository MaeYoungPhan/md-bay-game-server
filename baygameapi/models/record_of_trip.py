from django.db import models

class RecordOfTrip(models.Model):
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=False)
    name = models.CharField(max_length=55)
    occasion = models.ForeignKey("Occasion", on_delete=models.DO_NOTHING)
    number_found = models.IntegerField()
