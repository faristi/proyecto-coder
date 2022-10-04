from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Familiar(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    fecha_ingreso = models.DateField()