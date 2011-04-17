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

email = "Dirección de correo"
Abstract = \
    """This is a simple example document that illustrates how to put together a basic PDF with a chart.
I used the PLATYPUS library, which is part of ReportLab, and the charting capabilities built into ReportLab."""
Elements = []
HeaderStyle = styles['Heading1']
ParaStyle = styles['Normal']
PreStyle = styles['Code']


def header(txt, style=HeaderStyle, klass=Paragraph, sep=0.3, ):
    s = Spacer(0.2 * inch, sep * inch)
    para = klass(txt, style)
    sect = [s, para]
    result = KeepTogether(sect)
    return result


def p(txt):
    return header(txt, style=ParaStyle, sep=0.1)


def pre(txt):
    s = Spacer(0.1 * inch, 0.1 * inch)
    p = Preformatted(txt, PreStyle)
    precomps = [s, p]
    result = KeepTogether(precomps)
    return result


def go():
    doc = SimpleDocTemplate('ejemplo-03.pdf')
    doc.build(Elements)


mytitle = header(Title)
myname = header(Author, sep=0.1, style=ParaStyle)
mysite = header(URL, sep=0.1, style=ParaStyle)
mymail = header(email, sep=0.1, style=ParaStyle)
abstract_title = header('ABSTRACT')
myabstract = p(Abstract)
head_info = [mytitle, myname, mysite, mymail, abstract_title, myabstract, ]
Elements.extend(head_info)

code_title = header('Basic code to produce output')
code_explain = \
    p("""This is a snippet of code. It's an example using the Preformatted flowable object, which makes it easy to put code into your documents. Enjoy!""")
code_source = \
    pre("""
def header(txt, style=HeaderStyle, klass=Paragraph, sep=0.3):
    s = Spacer(0.2*inch, sep*inch)
    para = klass(txt, style)
    sect = [s, para]
    result = KeepTogether(sect)
    return result

def p(txt):
    return header(txt, style=ParaStyle, sep=0.1)

def pre(txt):
    s = Spacer(0.1*inch, 0.1*inch)
    p = Preformatted(txt, PreStyle)
    precomps = [s,p]
    result = KeepTogether(precomps)
    return result

def go():
    doc = SimpleDocTemplate('gfe.pdf')
    doc.build(Elements)
    """)
codesection = [code_title, code_explain, code_source]
src = KeepTogether(codesection)
Elements.append(src)
go()
