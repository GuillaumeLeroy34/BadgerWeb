from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    rfid = models.CharField(max_length=100)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    nombrePassage = models.IntegerField(default=0)
    estAutorise = models.BooleanField(default=False)
    def __str__(self): #définit ce qui va être affiché dans la console admin développeur
        return f"{self.prenom} {self.nom} id:{self.id}"
