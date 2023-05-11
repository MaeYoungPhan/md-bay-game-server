from django.db import models
from django.contrib.auth.models import User

class JokeReaction(models.Model):
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE, related_name='gamer_reacted')
    reaction = models.ForeignKey("Reaction", on_delete=models.SET_NULL, related_name='selected_reaction', null=True)
    joke = models.ForeignKey("Joke", on_delete=models.SET_NULL, related_name='selected_joke', null=True)
