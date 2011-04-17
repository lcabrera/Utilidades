#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Ejemplos tomados de:
http://www.protocolostomy.com/2008/10/22/generating-reports-with-charts-using-python-reportlab/
'''

from reportlab.platypus import *
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch

PAGE_HEIGHT = defaultPageSize[1]
styles = getSampleStyleSheet()
Title = 'Generating Reports with Python'
Author = 'Brian K. Jones'

# URL = "<a class="linkclass" href="http://www.protocolostomy.com">http://www.protocolostomy.com</a>"

URL = 'Enlace de Internet'

# email = "<a class="linkclass" href="mailto:bkjones@gmail.com">bkjones@gmail.com</a>"

email = 'eMail'

Abstract = 'This is a simple example document that illustrates how to put together a basic PDF with a chart. I used the PLATYPUS library, which is part of ReportLab, and the charting capabilities built into ReportLab.'

Elements = []
HeaderStyle = styles['Heading1']
ParaStyle = styles['Normal']
PreStyle = styles['Code']


def header(txt, style=HeaderStyle, klass=Paragraph, sep=0.3,):
    s = Spacer(0.2 * inch, sep * inch)
    Elements.append(s)
    para = klass(txt, style)
    Elements.append(para)


def p(txt):
    return header(txt, style=ParaStyle, sep=0.1)


def go():
    doc = SimpleDocTemplate('ejemplo-02.pdf')
    doc.build(Elements)


header(Title)
header(Author, sep=0.1, style=ParaStyle)
header(URL, sep=0.1, style=ParaStyle)
header(email, sep=0.1, style=ParaStyle)
header('ABSTRACT')
p(Abstract)

go()
