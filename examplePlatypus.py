__author__ = 'oquintansocampo'

import os
from reportlab.platypus import Paragraph
from reportlab.platypus import Image
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

follaEstilo = getSampleStyleSheet()

guion = []
cabecera = follaEstilo['Heading4']
cabecera.pageBreakBefore = 0
cabecera.keepWithNext = 1
cabecera.backColor = colors.blue

parrafo = Paragraph("CABECERA DEL DOCUMENTO", cabecera)

guion.append(parrafo)

documento = SimpleDocTemplate("exemplo2.pdf", pagesize=A4, showBoundary=0)
documento.build(guion)
