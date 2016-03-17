__author__ = 'oquintansocampo'

import os
from reportlab.platypus import Paragraph
from reportlab.platypus import Image
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Spacer
from reportlab.platypus import Table

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

import sqlite3 as dbapi

bbdd = dbapi.connect("bbdd.dat")
cursor = bbdd.cursor()
# cursor.execute("create table usuarios (id Integer,nome text)")
# cursor.execute("insert into usuarios values(1,'Oscar')")
# cursor.execute("insert into usuarios values(2,'Miguel')")
# cursor.execute("insert into usuarios values(3,'Fran')")
cursor.execute("select * from usuarios")
taboaBaseDatos = []

for fila in cursor:
    taboaBaseDatos.append(fila)

taboa = Table(taboaBaseDatos)

guion = []
guion.append(taboa)

documento = SimpleDocTemplate("exemplo2.pdf", pagesize=A4, showBoundary=0)
documento.build(guion)
cursor.close()
bbdd.close()
