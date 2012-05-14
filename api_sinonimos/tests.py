from sinonimos import app

import unittest
import json


class TestDiccionarioSinonimosAntonimos(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_si_paso_una_palabra_conocida_me_devuelve_un_sinonimo_valido(self):
        self.assertSinonimo('hola', 'shalom')

    def test_si_paso_una_palabra_desconocida_a_sinonimos_me_devuelve_null(self):
        self.assertSinonimo('nada', None)

    def test_una_palabra_puede_tener_varios_sinonimos(self):
        self.assertSinonimo('bleh', ['blah', 'bluh'])

    def test_si_paso_una_palabra_conocida_me_devuelve_un_antonimo_valido(self):
        self.assertAntonimo('chau', 'shalom')

    def test_si_paso_una_palabra_desconocida_a_antonimos__me_devuelve_null(self):
        self.assertAntonimo('nada', None)

    def test_una_palabra_puede_tener_varios_antonimos(self):
        self.assertAntonimo('bleh', ['foo', 'bar'])

    def assertSinonimo(self, palabra_a_buscar, sinonimos_esperados):
        self.assertDiccionario('sinonimos', palabra_a_buscar, sinonimos_esperados)

    def assertAntonimo(self, palabra_a_buscar, antonimos_esperados):
        self.assertDiccionario('antonimos', palabra_a_buscar, antonimos_esperados)

    def assertDiccionario(self, tipo_busqueda, palabra_a_buscar, esperados):
        response = json.loads(self.client.get('/%s/%s' % (tipo_busqueda, palabra_a_buscar,)).data)
        self.assertEquals(response['buscada'], palabra_a_buscar)
        self.assertEquals(response[tipo_busqueda], esperados)

if __name__ == '__main__':
    unittest.main()
