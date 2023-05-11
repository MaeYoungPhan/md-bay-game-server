from django.db import models
from django.contrib.auth.models import User

class FoundSiteItem(models.Model):
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE, related_name='gamer_site')
    bay_site_item = models.ForeignKey("BaySiteItem", on_delete=models.SET_NULL, related_name='site_item_found', null=True)
