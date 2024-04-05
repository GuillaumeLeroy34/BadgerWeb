from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    rfid = models.CharField(max_length=100)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    nombrePassage = models.IntegerField()
    estAutorise = models.BooleanField()
