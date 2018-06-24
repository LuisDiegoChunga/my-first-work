from django.db import models
from django.utils import timezone

# Create your models here.
class Ingresar_variables(models.Model):
    bolsas = models.IntegerField()
    sexo = models.IntegerField()
    edad = models.IntegerField()
    peso = models.IntegerField()
    diagnostico = models.IntegerField()
    servicio = models.IntegerField()
    hemoglobina = models.FloatField()
    hematocrito = models.IntegerField()
    gs_receptor = models.IntegerField()
    gs_donante = models.IntegerField()
    hiv = models.FloatField()
    hb = models.FloatField()
    anti_hb = models.FloatField()
    anti_hcv = models.FloatField()
    htlv = models.FloatField()
    sifilis = models.FloatField()
    chagas = models.FloatField()
    