from django.db import models

class Player (models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    country = models.CharField(max_length=50)
    position = models.CharField(max_length=2)
    team = models.CharField(max_length=50)

class NationalTeam(models.Model):
    name = models.CharField(max_length=50)
    worldcup_won = models.IntegerField()
    worldcup_played = models.IntegerField()
    #agregar funcion que diga que jugadores tenés de esta selección

class Stadium(models.Model):
    name = models.CharField(max_length=50)
    capacity = models.IntegerField()
    city = models.CharField(max_length=50)
   
