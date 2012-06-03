#!/usr/bin/python
# -*- coding: utf-8 -*-

#  This file is part of this project
#
# Copyright (C) 2011 Luis Cabrera <>
#
#  This library is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Library General Public
#  License as published by the Free Software Foundation; either
#  version 2 of the License, or (at your option) any later version.
#
#  This library is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  Library General Public License for more details.
#
#  You should have received a copy of the GNU Library General Public License
#  along with this library; see the file COPYING.LIB.  If not, write to
#  the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
#  Boston, MA 02110-1301, USA.
#


"""
# ~ código creado por: monobot.soft@gmail.com
# (www.alvarezalonso.es/monobotblog)
# ~ code by: monobot.soft@gmail.com
# (www.alvarezalonso.es/monobotblog)
"""

from reportlab.platypus import BaseDocTemplate
from reportlab.platypus import Paragraph
from reportlab.platypus import Spacer
from reportlab.platypus import Frame
from reportlab.platypus import PageTemplate
from reportlab.platypus import PageBreak
from reportlab.platypus import NextPageTemplate
from reportlab.platypus import Table, TableStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.graphics.shapes import Rect
from reportlab.lib.colors import tan

from reportlab.lib.pagesizes import A4
from reportlab.lib.pagesizes import A3
from reportlab.lib.pagesizes import landscape
from reportlab.lib.pagesizes import portrait
from reportlab.lib.units import cm

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFontFamily

import os
import time
from sys import modules as modules
from PIL import Image

# ~
# ~              D A T O S   G E N E R A L E S
# ~              V A R I A B L E S
# ~

#PAGINA = landscape(A4)
PAGINA = A4
EMAIL = 'lcabrera@sauco.org'
TITULO = 'Título de las pruebas'
SUBTITULO = 'Subtítulo de las pruebas'
TEMA = 'Pruebas sobre ReportLab'
AUTOR = 'Luis Cabrera Sauco'
PRODUCER = 'ReportLab y mucha paciencia'
KEYWORDS = 'ReportLab, PDF, Informes, etc'

LEFTMARGIN = 1 * cm
RIGHTMARGIN = -3 * cm
TOPMARGIN = 1 * cm
BOTTONMARGIN = 1 * cm

#A4 = (595.27559055118104, 841.88976377952747)
#CUERPO = [Paragraph( 'style': <ParagraphStyle ''> 'bulletT...tColor=Color(0,0,0,1), underline=0)] ) #Paragraph, Spacer(0, 28.3464566929), Paragraph( 'style': <ParagraphStyle ''> 'bulletT...tColor=Color(0,0,0,1), underline=0)] ) #Paragraph, <reportlab.platypus.doctemplate.NextPageTemplate instance>, PageBreak(), Paragraph( 'style': <ParagraphStyle ''> 'bulletT...tColor=Color(0,0,0,1), underline=0)] ) #Paragraph, Spacer(0, 56.6929133858), Table( rowHeights=[None, None, None, None, None...', '-4-1', '-3-1', '-2-1', '-1-1']] ) # end table, Spacer(0, 56.6929133858), Table( rowHeights=[None, None, None, None, None...', 'Hola', 'Hola', 'Hola', 'Hola']] ) # end table]
#DIA = time.struct_time(tm_year=2011, tm_mon=5, tm_mday...8, tm_sec=32, tm_wday=6, tm_yday=121, tm_isdst=1)
#DATA_T1 = [['00', '10', '20', '30', '...'], ['01', '11', '21', '...', '...'], ['02', '12', '...', '...', '-1-4'], ['03', '...', '...', '-2-3', '-1-3'], ['...', '...', '-3-2', '-2-2', '-1-2'], ['...', '-4-1', '-3-1', '-2-1', '-1-1']]
#DATA_T2 = [['Hola', 'Hola', 'Hola', 'Hola', 'Hola', 'Hola', 'Hola'], ['Hola', 'Hola', 'Hola', 'Hola', 'Hola', 'Hola', 'Hola'], ['Hola', 'Hola', 'Hola', 'Hola', 'Hola', 'Hola', 'Hola'], ['Hola', 'Hola', 'Hola', 'Hola', 'Hola', 'Hola', 'Hola'], ['Hola', 'Hola', 'Hola', 'Hola', 'Hola', 'Hola', 'Hola'], ['Hola', 'Hola', 'Hola', 'Hola', 'Hola', 'Hola', 'Hola']]
EST_ = ''
#EST_1 = <ParagraphStyle ''>
#EST_2 = <ParagraphStyle ''>
#EST_3 = <ParagraphStyle ''>
#FRAME_A4 = <reportlab.platypus.frames.Frame instance>
#FRAME_A4CORTO = <reportlab.platypus.frames.Frame instance>
FUENTE = 'DejaVu'
#HOJA_MODERNA = <reportlab.platypus.doctemplate.BaseDocTemplate instance>
#HOY = 'Mayo 2011'
#MES = 5
#MES_SP = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
NOMBRE_FICHERO = 'skel_01.pdf'
ALTURA_PAGINA = PAGINA[1]
#ALTURA_PAGINA = 29.7 * cm
#ALTURA_PAGINA = 841.88976377952747
ANCHURA_PAGINA = PAGINA[0]
#ANCHURA_PAGINA = 21 * cm
#ANCHURA_PAGINA = 595.27559055118104
#PARRAFO_P1 = Paragraph( 'style': <ParagraphStyle ''> 'bulletT...tColor=Color(0,0,0,1), underline=0)] ) #Paragraph
#PARRAFO_P2 = Paragraph( 'style': <ParagraphStyle ''> 'bulletT...tColor=Color(0,0,0,1), underline=0)] ) #Paragraph
#PARRAFO_P3 = Paragraph( 'style': <ParagraphStyle ''> 'bulletT...tColor=Color(0,0,0,1), underline=0)] ) #Paragraph
#PORTADA = <reportlab.platypus.doctemplate.PageTemplate instance>
#RESTO_PAGINAS = <reportlab.platypus.doctemplate.PageTemplate instance>
#TABLA_T1 = Table( rowHeights=[None, None, None, None, None...', '-4-1', '-3-1', '-2-1', '-1-1']] ) # end table
#TABLA_T2 = Table( rowHeights=[None, None, None, None, None...', 'Hola', 'Hola', 'Hola', 'Hola']] ) # end table
#TIPOTABLA_LIMPIA = TableStyle( ('BOTTOMPADDING', (0, 0), (-1, -1), ...N', (1, 0), (1, -1), 'CENTER') ) # end TableStyle
#TIPOTABLA_MODERNA = TableStyle( ('BOTTOMPADDING', (0, 0), (-1, -1), ...('REPEAROWS', (0, 0), (1, -1)) ) # end TableStyle
#cm = 28.346456692913385
#modules = {'FixTk': <module 'FixTk' from '/usr/lib/python2.6/lib-tk/FixTk.py'>, 'PIL': <module 'PIL' from '/usr/lib/python2.6/dist-packages/PIL/__init__.py'>, 'PIL.Image': <module 'PIL.Image' from '/usr/lib/python2.6/dist-packages/PIL/Image.py'>, 'PIL.ImageColor': <module 'PIL.ImageColor' from '/usr/lib/python2.6/dist-packages/PIL/ImageColor.py'>, 'PIL.ImageMode': <module 'PIL.ImageMode' from '/usr/lib/python2.6/dist-packages/PIL/ImageMode.py'>, 'PIL.ImagePalette': <module 'PIL.ImagePalette' from '/usr/lib/python2.6/dist-packages/PIL/ImagePalette.py'>, 'PIL._imaging': <module 'PIL._imaging' from '/usr/lib/python2.6/dist-packages/PIL/_imaging.so'>, 'PIL.array': None, 'PIL.operator': None, 'PIL.os': None, ...}
#tan = Color(.823529,.705882,.54902,1)


# MODULO_ACTUAL = modules[__name__]
# print MODULO_ACTUAL

# ~ DIA DE HOY Y CONVERTIRLO A ESPAÑOL

DIA = time.localtime()
MES = DIA.tm_mon
MES_SP = [
    'Enero',
    'Febrero',
    'Marzo',
    'Abril',
    'Mayo',
    'Junio',
    'Julio',
    'Agosto',
    'Septiembre',
    'Octubre',
    'Noviembre',
    'Diciembre', ]

HOY = '%s %d' % (MES_SP[MES - 1], DIA.tm_year)
# NOMBRE_FICHERO = 'monobotblog.pdf'

# ~
# ~         C O N F I G U R A N D O    L A S   F U E N T E S
# ~

pdfmetrics.registerFont(TTFont('DejaVu',
    '/usr/share/fonts/truetype/ttf-dejavu/DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('DejaVuBd',
    '/usr/share/fonts/truetype/ttf-dejavu/DejaVuSans-Bold.ttf'))
pdfmetrics.registerFont(TTFont('DejaVuBdIt',
    '/usr/share/fonts/truetype/ttf-dejavu/DejaVuSans-Oblique.ttf'))
pdfmetrics.registerFont(TTFont('DejaVuIt',
    '/usr/share/fonts/truetype/ttf-dejavu/DejaVuSansCondensed-Oblique.ttf'))
registerFontFamily(
    'Dejavu',
    normal='DejaVu',
    bold='DejaVuBd',
    italic='DejaVuIt',
    boldItalic='DejaVuBdIt')

# ~
# ~          E S T A B L E C I E N D O   L O S   E S T I L O S
# ~
# ~              P A R R A F O S
# ~

EST_1 = ParagraphStyle('', fontName=FUENTE, fontSize=12, alignment=0)

EST_2 = ParagraphStyle('', fontName=FUENTE, fontSize=8, alignment=0)

EST_3 = ParagraphStyle(
    '',
    fontName=FUENTE,
    fontSize=6,
    alignment=0,
    leftIndent=cm,
    bulletIndent=0.5 * cm, )

# ~
# ~              T A B L A S
# ~

TIPOTABLA_MODERNA = TableStyle([
    ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
    ('TOPPADDING', (0, 0), (-1, -1), 1),
    ('LEFTPADDING', (0, 0), (-1, -1), 3),
    ('RIGHTPADDING', (0, 0), (-1, -1), 3),
    ('FONT', (0, 0), (-1, -1), FUENTE, 8),
    ('GRID', (0, 0), (-1, -1), 0.01 * cm, 'Black'),
    ('FONT', (0, 0), (0, -1), FUENTE, 15),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('ALIGN', (0, 0), (0, -1), 'RIGHT'),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('SPAN', (0, 0), (0, -1)),
    ('REPEAROWS', (0, 0), (1, -1)),
    ])

TIPOTABLA_LIMPIA = TableStyle([
    ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
    ('TOPPADDING', (0, 0), (-1, -1), 1),
    ('LEFTPADDING', (0, 0), (-1, -1), 3),
    ('RIGHTPADDING', (0, 0), (-1, -1), 3),
    ('TEXTCOLOR', (0, 0), (-1, -1), 'Grey'),
    ('FONT', (0, 0), (-1, -1), FUENTE, 10),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('ALIGN', (-1, 0), (-1, -1), 'RIGHT'),
    ('ALIGN', (1, 0), (1, -1), 'CENTER'),
    ])

##############################################################################
#def buildDocTemplate(fname, indexer):
#    dt = BaseDocTemplate(fname)
#    sb = 0
#
#    address = Frame(dt.leftMargin + 8*cm, PAGINA[1] - 9.5*cm, 7*cm, 4*cm, id = 'address', showBoundary = sb)
#    additional = Frame(0, PAGINA[1] - 5.6*cm, 7*cm, 1*cm, id = 'additional', showBoundary = sb)
#    summary = Frame(1*cm, 1*cm, PAGINA[1] - 2*cm, PAGINA[0] - 2*cm, id = 'summary', showBoundary= sb)
#    bollettini1 = Frame(-0.55*cm, (PAGINA[0] / 2) + 0.15*cm, PAGINA[1], PAGINA[0]/2 - 1*cm, id = 'bollettini1', showBoundary = sb)
#    bollettini2 = Frame(-0.55*cm, 0.2*cm, PAGINA[1], PAGINA[0]/2 - 1.4*cm, id = 'bollettini2', showBoundary = sb)
#
#    dt.addPageTemplates(
#    	[
#    		 PageTemplate(id='address',    frames=[additional,address],                         onPageEnd=indexer.addressPage),
#            PageTemplate(id='summary',    frames=summary,                   onPage=_landscape, onPageEnd=indexer.summaryPage),
#            PageTemplate(id='bollettini', frames=[bollettini1,bollettini2], onPage=_landscape, onPageEnd=indexer.ccpPage),
#       ])
#
#    return dt
##############################################################################

# ~
# ~              C A N V A S
# ~
def pagina_cabecera(canvas, hoja_moderna):
    '''Definición de estilo de página.'''

    canvas.saveState()
    canvas.setFont(FUENTE, 5)
    canvas.drawRightString(ANCHURA_PAGINA - 1 * cm, ALTURA_PAGINA - 1 * cm, '%s' % HOY)
    canvas.drawRightString(ANCHURA_PAGINA - 1 * cm, ALTURA_PAGINA - 1.2 * cm, EMAIL)
    canvas.setFont(FUENTE, 15)
    canvas.drawString(4.7 * cm, ALTURA_PAGINA - 1.5 * cm, TITULO)
    canvas.restoreState()


def resto_paginas(canvas, hoja_moderna):
    '''Definición de estilo de página.'''

    canvas.saveState()
    canvas.setFont(FUENTE, 5)
    canvas.drawRightString(ANCHURA_PAGINA - 1 * cm, ALTURA_PAGINA - 1 * cm, '%s' % HOY)
    canvas.drawRightString(ANCHURA_PAGINA - 1 * cm, ALTURA_PAGINA - 1.2 * cm, EMAIL)
    canvas.setFont(FUENTE, 15)
    canvas.drawString(4.7 * cm, ALTURA_PAGINA - 1.5 * cm, SUBTITULO)
    canvas.setFont(FUENTE, 8)
    canvas.drawCentredString(ANCHURA_PAGINA/2, 0.75 * cm, "%d" % (hoja_moderna.page))
    canvas.restoreState()

def _landscape(canvas, hoja_moderna):
    '''Snippet para generar páginas apaisadas.'''

    #canvas.saveState()
    canvas.rotate(90)
    canvas.translate(0, -PAGINA[0])
    canvas.setFont(FUENTE, 8)
    canvas.drawCentredString(ALTURA_PAGINA/2, 0.60 * cm, "%d" % (hoja_moderna.page))
    #canvas.restoreState()

# ~
# ~              F R A M E S
# ~

# Corto, para portadas o similares:
FRAME_CORTO = Frame(
    x1 = 1 * cm,
    y1 = 1 * cm,
    width = ANCHURA_PAGINA - 2 * cm,
    height = ALTURA_PAGINA - 10 * cm,
    showBoundary = 0)

# Normal, para páginas normales:
FRAME_NORMAL = Frame(
    x1 = 1 * cm,
    y1 = 1 * cm,
    width = ANCHURA_PAGINA - 2 * cm,
    height = ALTURA_PAGINA - 4 * cm,
    showBoundary = 0)

# Apaisado, para tablas y gráficos pesados:
FRAME_APAISADO = Frame(
    x1 = 1 * cm,
    y1 = 1 * cm,
    width = ALTURA_PAGINA - 2 * cm,
    height = ANCHURA_PAGINA - 2 * cm,
    showBoundary = 1)

# ~
# ~              P A G I N A S
# ~
PORTADA = PageTemplate(
    id = '1era_pag',
    frames = FRAME_CORTO,
    onPage = pagina_cabecera)

RESTO_PAGINAS = PageTemplate(
    id = 'resto',
    frames = FRAME_NORMAL,
    onPage = resto_paginas)

PAGINAS_APAISADAS = PageTemplate(
    id = 'apaisada',
    frames = FRAME_APAISADO,
    #onPage = _landscape(canvas, CUERPO))
    onPage = _landscape)

# ~
# ~ estilos DE DOCUMENTOS
# ~

HOJA_MODERNA = BaseDocTemplate(
    NOMBRE_FICHERO,
    pagesize = PAGINA,
    pageTemplates = [RESTO_PAGINAS, PAGINAS_APAISADAS, PORTADA],
    showBoundary = 0,
    leftMargin = LEFTMARGIN,
    rightMargin = RIGHTMARGIN,
    topMargin = TOPMARGIN,
    bottomMargin = BOTTONMARGIN,
    allowSplitting = 1,
    title = TITULO,
    subject = TEMA,
    author = AUTOR,
    producer = PRODUCER,
    keywords = KEYWORDS,
    _pageBreakQuick = 1,
    encrypt = None)

# ~
# ~      C R E A M O S   E L   C U E R P O   D E L   M E N S A J E
# ~  Y   A Ñ A D I M O S  T E X T O  P A R A  P R U E B A S
# ~

CUERPO = []
PARRAFO_P1 = Paragraph('Este es el texto del parrafo 1' * 50, EST_1)
PARRAFO_P2 = Paragraph('Este es el texto del parrafo 2' * 50, EST_2)
PARRAFO_P3 = Paragraph('Este es el texto del parrafo 3' * 50, EST_3)

CUERPO.append(PARRAFO_P1)
CUERPO.append(Spacer(0, 1 * cm))
CUERPO.append(PARRAFO_P2)
CUERPO.append(NextPageTemplate('resto'))
CUERPO.append(PageBreak())
CUERPO.append(PARRAFO_P3)
CUERPO.append(Spacer(0, 2 * cm))

DATA_T1 = [
    ['00', '10', '20', '30', '...'],
    ['01', '11', '21', '...', '...'],
    ['02', '12', '...', '...', '-1-4'],
    ['03', '...', '...', '-2-3', '-1-3'],
    ['...', '...', '-3-2', '-2-2', '-1-2'],
    ['...', '-4-1', '-3-1', '-2-1', '-1-1'], ]

TABLA_T1 = Table(DATA_T1, style = TIPOTABLA_LIMPIA)

CUERPO.append(TABLA_T1)

# Experimento: Una tabla dentro de un párrafo...
#PARRAFO_T1 = Paragraph(TABLA_T1, EST_1)
#CUERPO.append(PARRAFO_T1)

CUERPO.append(Spacer(0, 2 * cm))

DATA_T2 = [
    ['Hola', 'Hola', 'Hola', 'Hola', 'Hola', 'Hola', 'Hola', ],
    ['Hola', 'Hola', 'Hola', 'Hola', 'Hola', 'Hola', 'Hola', ],
    ['Hola', 'Hola', 'Hola', 'Hola', 'Hola', 'Hola', 'Hola', ],
    ['Hola', 'Hola', 'Hola', 'Hola', 'Hola', 'Hola', 'Hola', ],
    ['Hola', 'Hola', 'Hola', 'Hola', 'Hola', 'Hola', 'Hola', ],
    ['Hola', 'Hola', 'Hola', 'Hola', 'Hola', 'Hola', 'Hola', ], ]

TABLA_T2 = Table(DATA_T2, style = TIPOTABLA_MODERNA)

CUERPO.append(TABLA_T2)

# Añadido para probar paginas apaisadas
CUERPO.append(NextPageTemplate('apaisada'))
CUERPO.append(PageBreak())
CUERPO.append(PARRAFO_P1)
CUERPO.append(Spacer(0, 1 * cm))
CUERPO.append(PARRAFO_P2)
CUERPO.append(PARRAFO_P3)
CUERPO.append(Spacer(0, 2 * cm))
CUERPO.append(PARRAFO_P3)
CUERPO.append(Spacer(0, 2 * cm))
CUERPO.append(PARRAFO_P1)
CUERPO.append(Spacer(0, 1 * cm))
CUERPO.append(PARRAFO_P2)
CUERPO.append(NextPageTemplate('resto'))
CUERPO.append(PageBreak())
CUERPO.append(PARRAFO_P3)
CUERPO.append(Spacer(0, 2 * cm))
CUERPO.append(PARRAFO_P3)
CUERPO.append(Spacer(0, 2 * cm))
CUERPO.append(PARRAFO_P3)
CUERPO.append(Spacer(0, 2 * cm))

def construir_pdf():
    '''Lanzamos el código.'''

    HOJA_MODERNA.build(CUERPO)
    # Lanzar un visor de pdf
    # os.startfile(NOMBRE_FICHERO)


if __name__ == '__main__':
    construir_pdf()
