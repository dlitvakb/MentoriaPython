from django.test import TestCase
from django.test.client import Client

class DetalleDeGastosTest(TestCase):
    def test_si_no_estoy_logueado_me_tiene_que_rebotar(self):
        c = Client()
        response = c.get('/detalle/')
        self.assertEqual(401, response.status_code)

    def test_si_estoy_logueado_puedo_ver_el_detalle(self):
        client = Client()
        import ipdb; ipdb.set_trace()
        client.post('/accounts/login/', {'username': 'dave', 'password': 'sa'})
        response = client.get('/detalle/')
        self.assertEqual(200, response.status_code)
