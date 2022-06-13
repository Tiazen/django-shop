from statistics import mode
from django.db import models

class ShopModel(models.Model):
    """
    Model to represent a shop.
    """
    name = models.CharField("Shop name", max_length=50)
    description = models.CharField("Shop Description", max_length=1200)