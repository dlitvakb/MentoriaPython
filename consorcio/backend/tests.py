"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from models import Departamento

class TestXXXX(TestCase):
    def test_un_departamento_tiene_un_identificador_y_su_representacion_es_dicho_identificador(self):
        departamento = Departamento(identificador="1 b")
        self.assertEqual("1 b", str(departamento))
