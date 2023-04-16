from django.shortcuts import render
from datetime import datetime
import sqlite3

conn = sqlite3.connect("db.sqlite3")

cur = conn.cursor()

# cur.execute("SELECT * FROM core_feriadomodel WHERE dia = " 
#              + str(datetime.now().day) + " AND mes = " 
#              + str(datetime.now().month))

cur.execute("SELECT * FROM core_feriadomodel WHERE dia = 25 AND mes = 12")

fetch = cur.fetchall()

contexto = {
    "feriado": "Não é feriado"
}

if len(fetch) >= 1:
    contexto = {
        "feriado" : str("Hoje é " + fetch[0][1])
    }


def index(request):
    return render(request, 'index.html', contexto)