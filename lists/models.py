from django.db import models


class List(models.Model):
    """Список"""
    pass


class Item(models.Model):
    """Элемент списка"""
    text = models.TextField(default='', null=True)
    list = models.ForeignKey(List, on_delete=models.CASCADE, default=None)
