#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Ejemplos tomados de:
http://www.protocolostomy.com/2008/10/22/generating-reports-with-charts-using-python-reportlab/
'''

from reportlab.platypus import *
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.rl_config import defaultPageSize
#from reportlab.lib.units import inch

PAGE_HEIGHT = defaultPageSize[1]

#URL_DIR = "<a class=\"linkclass\" href=\"http://www.protocolostomy.com\">http://www.protocolostomy.com</a>"
URL_DIR = "Texto simple"

ABSTRACT_TEXT = "This is a simple example document that illustrates how " \
"to put together a basic PDF with a chart. I used the PLATYPUS library, "\
"which is part of ReportLab, and the charting capabilities built into ReportLab."

STYLES = getSampleStyleSheet()

TITLE = Paragraph('Generating Reports with Python', STYLES['Heading1'])

AUTHOR = Paragraph('Brian K. Jones', STYLES['Normal'])

URL = Paragraph(URL_DIR, STYLES['Normal'])

EMAIL = Paragraph('bkjones +_at_+ gmail.com', STYLES['Normal'])
ABSTRACT = Paragraph(ABSTRACT_TEXT, STYLES['Normal'])

ELEMENTS = [TITLE, AUTHOR, URL, EMAIL, ABSTRACT]


def go_pdf():
    '''Compilamos el PDF.'''

    doc = SimpleDocTemplate('ejemplo-01.pdf')
    doc.build(ELEMENTS)

go_pdf()
