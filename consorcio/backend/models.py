from django.db import models
from validators import validate_not_empty_string
from django.core.exceptions import ValidationError

class Departamento(models.Model):
    identificador = models.CharField(max_length=30, null=False, blank=False, validators=[validate_not_empty_string])
    metraje = models.IntegerField()
    propietario = models.ForeignKey('Propietario')
    edificio = None

    def __str__(self):
        return self.identificador

    def validate_departamento_pertenece_a_un_edificio(self):
        if self.edificio is None:
            raise ValidationError("No tiene un edificio asignado")

    def save(self):
        self.validate_departamento_pertenece_a_un_edificio()
        validate_not_empty_string(self.identificador)
        super(Departamento, self).save()

class Propietario(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    dni = models.IntegerField()

class Edificio(models.Model):
    numero = models.IntegerField()
    direccion = models.CharField(max_length=60, null=False, blank=False, validators=[validate_not_empty_string])
    departamentos = models.ForeignKey('')


