from django.db import models

class Departamento(models.Model):
    identificador = models.CharField(max_length=30, blank=False)

    def __str__(self):
        return self.identificador
