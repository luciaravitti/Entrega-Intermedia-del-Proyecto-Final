from django.db import models

# Create your models here.

class Entrada(models.Model):
    nombre= models.CharField(max_length=50)
    vegano=models.BooleanField()
    cantidad_personas=models.IntegerField()

    def __str__(self):
        return self.nombre

class Principal(models.Model):
    nombre= models.CharField(max_length=50)
    vegano= models.BooleanField()
    cantidad_personas=models.IntegerField()

    def __str__(self):
        return self.nombre

class Postre(models.Model):
    nombre= models.CharField(max_length=50)
    vegano=models.BooleanField()
    cantidad_personas=models.IntegerField()

    def __str__(self):
        return self.nombre
