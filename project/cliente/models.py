from django.db import models

class Pais(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.nombre
    
class cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    pais_origen = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class juegos(models.Model):
    nombre_juego = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre_juego} {self.genero}"



    
