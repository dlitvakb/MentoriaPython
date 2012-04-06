"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from models import Departamento, Propietario, Edificio
from django.core.exceptions import ValidationError

class TestDepartamento(TestCase):
    def test_un_departamento_tiene_un_identificador_y_su_representacion_es_dicho_identificador(self):
        departamento = Departamento(identificador="1 b")
        self.assertEqual("1 b", str(departamento))

    def test_un_departamento_tiene_metraje(self):
        departamento = Departamento(metraje=25)
        self.assertEqual(25, departamento.metraje)

    def test_un_departamento_tiene_un_propietario(self):
        departamento = Departamento(
                         propietario=Propietario(
                           nombre="Pepe Morales",
                           dni=35227937
                         )
                       )
        self.assertEqual("Pepe Morales", departamento.propietario.nombre)
        self.assertEqual(35227937, departamento.propietario.dni)

    def test_si_un_departamento_no_tiene_identificador_no_es_valido(self):
        propietario = Propietario(nombre="Pepe Morales", dni=35227937)
        propietario.save()
        departamento = Departamento(metraje=25, propietario=propietario)
        with self.assertRaises(ValidationError):
            departamento.save()

    def test_un_departamento_debe_validar_integridad_en_sus_campos(self):
        propietario = Propietario(nombre="Pepe Morales", dni=35227937)
        propietario.save()
        departamento = Departamento(
                         identificador="1 b",
                         metraje=25,
                         propietario=propietario,
                        )
        departamento.edificio = 1
        departamento.save()
        # si llego hasta aca es que valido

    def test_un_departamente_debe_pertenecer_a_un_edificio(self):
        propietario = Propietario(nombre="Pepe Morales", dni=35227937)
        propietario.save()
        departamento = Departamento(
                         identificador="1 b",
                         metraje=25,
                         propietario=propietario
                       )
        with self.assertRaises(ValidationError):
            departamento.save()

    def test_quiero_que_el_edificio_sea_posta_posta_un_elemento_persistente(self):
        propietario = Propietario(nombre="Pepe Morales", dni=35227937)
        propietario.save()
        departamento = Departamento(
                         identificador="1 b",
                         metraje=25,
                         propietario=propietario,
                        )
        edificio = Edificio(direccion="santa fe", numero=3433)
        edificio.departamentos.append(departamento)
        edificio.save()
        departamento.edificio = edificio
        departamento.save()

        departamento_from_db = Departamento.objects.get(
                                 identificador="1 b"
                               )
        self.assertEqual(edificio, departamento_from_db.edificio)


class TestEdificio(TestCase):
    def test_un_edificio_debe_tener_direccion(self):
        edificio = Edificio(direccion="santa fe", numero=3433)
        edificio.save()
        # si llego hasta aca es valido


    def test_un_edificio_si_no_tiene_direccion_explota(self):
        edificio = Edificio()
        with self.assertRaises(Exception):
            edificio.save()

    def test_un_edificio_puede_tener_departamentos(self):
        propietario = Propietario(nombre="Pepe Morales", dni=35227937)
        propietario.save()
        departamento = Departamento(
                         identificador="1 b",
                         metraje=25,
                         propietario=propietario,
                        )
        edificio = Edificio(direccion="santa fe", numero=3433)
        edificio.departamentos.append(departamento)
        edificio.save()
        departamento.edificio = edificio
        departamento.save()
        self.assertTrue(departamento in departamento.edificio.departamentos)


