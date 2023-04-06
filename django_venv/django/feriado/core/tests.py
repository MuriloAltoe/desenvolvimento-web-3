from django.test import TestCase
from core.models import FeriadoModel
from datetime import datetime


class NatalTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/natal')
    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)
    def test_texto(self):
        self.assertContains(self.resp, 'natal')

class TiradentesTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/tiradentes')
    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)
    def test_texto(self):
        self.assertContains(self.resp, 'tiradentes')


def test_created(self):
    self.assertTrue(FeriadoModel.objects.exists())
def test_modificado_em(self):
    self.assertIsInstance(self.cadastro.modificado_em, datetime)
def test_nome_feriado(self):
    nome = self.cadastro.__dict__.get('nome', '')
    self.assertEqual(nome, self.feriado)
def test_dia_feriado(self):
    dia = self.cadastro.__dict__.get('dia', '')
    self.assertEqual(dia, self.dia)