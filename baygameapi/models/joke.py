from django.db import models

class Joke(models.Model):
    title = models.CharField(max_length = 50)
    question = models.CharField(max_length=750)
    answer = models.CharField(max_length=750)
