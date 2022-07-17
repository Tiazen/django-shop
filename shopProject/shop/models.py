from statistics import mode
from unicodedata import category
from django.db import models
from users.models import User

class ShopCategory(models.Model):
    """
    Model to represent categories of shops
    """
    name = models.CharField('Shop category', max_length=120)
    active = models.BooleanField(default=True)


class ItemCategory(models.Model):
    """
    Model to represent categories of items
    """
    name = models.CharField('Item category', max_length=120)


class ShopModel(models.Model):
    """
    Model to represent a shop. 
    """
    name = models.CharField("Shop name", max_length=50)
    description = models.CharField("Shop Description", max_length=1200)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(to=ShopCategory)


class ShopItem(models.Model):
    shop = models.ForeignKey(to=ShopModel, on_delete=models.CASCADE)
    category = models.ForeignKey(to=ItemCategory, on_delete=models.SET_NULL, null=True)
    name = models.CharField("item name", max_length=250)
    amount = models.IntegerField("Amount of items", default=0)
    color = models.CharField("Color", max_length=120, default="None")
