from django.db import models, IntegrityError
from validators import validate_not_empty_string
from django.core.exceptions import ValidationError, ObjectDoesNotExist

class Departamento(models.Model):
    identificador = models.CharField(max_length=30, null=False, blank=False, validators=[validate_not_empty_string])
    metraje = models.IntegerField()
    propietario = models.ForeignKey('Propietario')
    edificio = models.ForeignKey('Edificio')

    def __str__(self):
        return "%s %s - %s" % (self.edificio.direccion,
                               self.edificio.numero,
                               self.identificador)

    def validate_departamento_pertenece_a_un_edificio(self):
        try:
            return self.edificio
        except ObjectDoesNotExist:
            raise ValidationError("No tiene un edificio asignado")

    def save(self):
        self.validate_departamento_pertenece_a_un_edificio()
        validate_not_empty_string(self.identificador)
        super(Departamento, self).save()

class Propietario(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    dni = models.IntegerField(primary_key=True)

    def validate_dni_unique(self):
        propietarios = Propietario.objects.all()
        todos_los_dnis = [ propietario.dni for propietario in propietarios ]
        if self.dni in todos_los_dnis:
            raise IntegrityError('El DNI ya existe')

    def validates_dni(self):
        if self.dni is None:
            raise ValidationError('No hay un DNI')
        elif self.dni <= 0:
            raise ValidationError('El DNI no es Vallido')
        self.validate_dni_unique()

    def save(self):
        self.validates_dni()
        super(Propietario, self).save()

    def __str__(self):
        return "%s - %s" % (self.dni, self.nombre)

class Edificio(models.Model):
    direccion = models.CharField(max_length=60, null=False, blank=False, validators=[validate_not_empty_string])
    numero = models.IntegerField()

    @property
    def departamentos(self):
        return self.departamento_set

    def __str__(self):
        return "%s %s" % (self.direccion, self.numero)
