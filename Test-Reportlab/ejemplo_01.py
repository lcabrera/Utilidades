#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Ejemplos tomados de:
http://www.protocolostomy.com/2008/10/22/generating-reports-with-charts-using-python-reportlab/
'''

#from reportlab.platypus import *
from reportlab.platypus import Paragraph
from reportlab.platypus import Spacer
from reportlab.platypus import Table
from reportlab.platypus import SimpleDocTemplate

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.rl_config import defaultPageSize
# from reportlab.lib.units import inch

from reportlab.lib import colors

PAGE_HEIGHT = defaultPageSize[1]

# URL_DIR = "<a class=\"linkclass\" href=\"http://www.protocolostomy.com\">http://www.protocolostomy.com</a>"

URL_DIR = 'Texto simple'

ABSTRACT_TEXT = \
    'This is a simple example document that illustrates how to put together a basic PDF with a chart. I used the PLATYPUS library, which is part of ReportLab, and the charting capabilities built into ReportLab.'

FILA1 = ['', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo', ]
FILA2 = ['Mañana', 'Estudiar', 'Gimnasio', '-', '-', '-', 'Estudiar', 'Ir a la iglesia', ]
FILA3 = ['Tarde', 'Trabajar', 'Trabajar', 'Trabajar', 'Trabajar', 'Trabajar', '-', '-', ]
FILA4 = ['Noche', 'Trabajar', 'Trabajar', 'Trabajar', 'Trabajar', '-', '-', '-', ]

STYLES = getSampleStyleSheet()

TITLE = Paragraph('Generating Reports with Python', STYLES['Heading1'])

AUTHOR = Paragraph('Brian K. Jones', STYLES['Normal'])

URL = Paragraph(URL_DIR, STYLES['Normal'])

EMAIL = Paragraph('bkjones +_at_+ gmail.com', STYLES['Normal'])

ABSTRACT = Paragraph(ABSTRACT_TEXT, STYLES['Normal'])

ELEMENTS = [TITLE, AUTHOR, URL, EMAIL, ABSTRACT]

ELEMENTS.append(Spacer(0, 20))

# Definimos la tabla.
TABLA = Table([FILA1, FILA2, FILA3, FILA4])

# Podemos dar estilo a los elementos de una tabla. En esta ocasión vamos a poner de color azul Mañana,Tarde y Noche y en color rojo los días de la semana.
TABLA.setStyle([
    ('GRID', (0, 0), (-1, -1), 0.2, colors.silver),
    ('TEXTCOLOR', (1, -4), (7, -4), colors.red),
    ('TEXTCOLOR', (0, 0), (0, 3), colors.blue)])

# Y la asignamos al platypus story.
ELEMENTS.append(TABLA)


def go_pdf():
    '''Compilamos el PDF.'''

    doc = SimpleDocTemplate('ejemplo-01.pdf')
    doc.build(ELEMENTS)


go_pdf()
