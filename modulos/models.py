from django.db import models
from cuentas.models import User


class Modulo(models.Model):
    usuario = models.ManyToManyField(User)
    nombre = models.CharField(max_length = 50)
    subtitulo = models.CharField(max_length = 50)
    descripcion = models.CharField(max_length = 100)
    img = models.CharField(max_length = 200, null = True)

    def __str__(self):
        return self.nombre


