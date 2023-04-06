from django.shortcuts import render
from datetime import datetime

from django.http import HttpResponse
from django.test import TestCase
from feriado.core.models import FeriadoModel

from datetime import datetime
class FeriadoModelTest(TestCase):
    def setUp(self):
        self.feriado = 'Natal'
        self.mes = 12
        self.dia = 25
        self.cadastro = FeriadoModel(
        nome=self.feriado,
        dia=self.dia,
        mes=self.mes,
        )
        self.cadastro.save()


contexto = {
    "natal":False,
    "tiradentes":False
}

def natal(request):
    if datetime.now().month == 12 and datetime.now().day == 25:
        contexto["natal"] = True
    return render(request, 'natal.html', contexto)

def tiradentes(request):
    if datetime.now().month == 4 and datetime.now().day == 21:
        contexto["tiradentes"] = True
    return render(request, 'tiradentes.html', contexto)


