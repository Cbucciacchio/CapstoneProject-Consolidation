# models.py
from django.db import models
from django.contrib.auth.models import User

class Set(models.Model):
    name = models.CharField(max_length=255)
    releaseDate = models.DateField(null=True, blank=True)
    logo = models.URLField(max_length=2000, null=True, blank=True)


    def __str__(self):
        return self.name

class Card(models.Model):
    name = models.CharField(max_length=100)
    set = models.ForeignKey(Set, on_delete=models.CASCADE, null=True, blank=True) 
    image = models.JSONField()  
    card_id = models.CharField(max_length=100, default='default_card_id')

class MyCollection(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cards = models.ManyToManyField(Card)




    