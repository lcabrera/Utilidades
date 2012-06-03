#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
# ~ código creado por: monobot.soft@gmail.com
# (www.alvarezalonso.es/monobotblog)
# ~ code by: monobot.soft@gmail.com
# (www.alvarezalonso.es/monobotblog)
"""

#import __future__

# Optimización de velocidad:
#import psyco
#psyco.profile()
############################

#import os
import time
#from sys import modules as modules
#from PIL import Image

from reportlab.platypus import BaseDocTemplate, Paragraph, Spacer, \
    Frame, PageTemplate, PageBreak, NextPageTemplate
from reportlab.platypus import Table, TableStyle
from reportlab.lib.styles import ParagraphStyle
#from reportlab.graphics.shapes import Rect
#from reportlab.lib.colors import tan

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFontFamily

# MODULO_ACTUAL = modules[__name__]
# print MODULO_ACTUAL

class MODELO(object):
    '''Clase PADRE para todos los modelos.'''

    # ~
    # ~              D A T O S   G E N E R A L E S
    # ~              V A R I A B L E S
    # ~

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
    NOMBRE_FICHERO = 'monobotblog.pdf'
    PAGE_HEIGHT = 29.7 * cm
    #PAGE_HEIGHT = 841.88976377952747
    PAGE_WIDTH = 21 * cm
    #PAGE_WIDTH = 595.27559055118104
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
    pass

    def __init__(self):

        #~
        #~  DIA DE HOY Y CONVERTIRLO A ESPAÑOL
        #~
        # self.EST_1 = 1

        self.DIA = time.localtime()
        self.MES = self.DIA.tm_mon
        self.MES_SP = [
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

        self.HOY = '%s %d' % (self.MES_SP[self.MES - 1], self.DIA.tm_year)

        #NOMBRE_FICHERO = 'monobotblog.pdf'

        # ~
        # ~ C O N F I G U R A N D O  L A S   F U E N T E S
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
        # ~ E S T A B L E C I E N D O   L O S   E S T I L O S
        # ~ P A R A  L O S  P A R R A F O S
        # ~

        self.EST_1 = ParagraphStyle(
            '',
            fontName = 'DejaVu',
            fontSize = 12,
            alignment=0)
        print type(self.EST_1)
        self.EST_2 = ParagraphStyle(
            '',
            fontName = 'DejaVu',
            fontSize = 8,
            alignment=0)
        self.EST_3 = ParagraphStyle(
            '',
            fontName = 'DejaVu',
            fontSize = 6,
            alignment = 0,
            leftIndent = cm,
            bulletIndent = 0.5 * cm, )

        # ~
        # ~ F R A M E S
        # ~

        self.FRAME_A4 = Frame(
            x1 = 1 * cm,
            y1 = 1 * cm,
            width = self.PAGE_WIDTH - 2 * cm,
            height = self.PAGE_HEIGHT - 4 * cm)

        self.FRAME_A4CORTO = Frame(
            x1 = 1 * cm,
            y1 = 1 * cm,
            width = self.PAGE_WIDTH - 2 * cm,
            height = self.PAGE_HEIGHT - 10 * cm)

        # ~
        # ~ P A G I N A S
        # ~

        self.PORTADA = PageTemplate(
            id = '1era_pag',
            frames = self.FRAME_A4CORTO,
            onPage = self.pagina_cabecera)

        self.RESTO_PAGINAS = PageTemplate(
            id = 'resto',
            frames = self.FRAME_A4,
            onPage = self.resto_paginas)

        # ~
        # ~ ESTILOS DE DOCUMENTOS
        # ~

        self.HOJA_MODERNA = BaseDocTemplate(
            MODELO.NOMBRE_FICHERO,
            pagesize = A4,
            pageTemplates = [MODELO.PORTADA, MODELO.RESTO_PAGINAS],
            showBoundary = 1,
            leftMargin = 1 * cm,
            rightMargin = -3 * cm,
            topMargin = 1 * cm,
            bottomMargin = 1 * cm,
            allowSplitting = 1,
            tittle = None,
            author = None,
            _pageBreakQuick = 1,
            encrypt = None, )

    def pagina_cabecera(self, canvas, hoja_moderna):
        '''Definición de estilo de página.'''

        canvas.saveState()

        #~
        #~    T E X T O S  C A B E C E R A
        #~

        canvas.setFont(self.FUENTE, 5)

        canvas.drawRightString(
                self.PAGE_WIDTH - 1 * cm,
                self.PAGE_HEIGHT - 1 * cm,
                'impresión: %s' % self.HOY)

        canvas.drawRightString(
                self.PAGE_WIDTH - 1 * cm,
                self.PAGE_HEIGHT - 1.2 * cm,
                'monobotblog.alvarezalonso.es')

        canvas.setFont(self.FUENTE, 15)

        canvas.drawString(
                4.7 * cm,
                self.PAGE_HEIGHT - 1.5 * cm,
                'Prueba Report Lab Hoja Primera')

        canvas.restoreState()

    def resto_paginas(self, canvas, hoja_moderna):
        '''Definición de estilo de página.'''

        canvas.saveState()

        #~
        #~  C A N V A S
        #~

        canvas.setFont(self.FUENTE, 5)

        canvas.drawRightString(
                self.PAGE_WIDTH - 1 * cm,
                self.PAGE_HEIGHT - 1 * cm,
                'impresión: %s' % self.HOY)

        canvas.drawRightString(
                self.PAGE_WIDTH - 1 * cm,
                self.PAGE_HEIGHT - 1.2 * cm,
                'monobotblog.alvarezalonso.es')

        canvas.setFont(self.FUENTE, 15)

        canvas.drawString(
                4.7 * cm,
                self.PAGE_HEIGHT - 1.5 * cm,
                'Prueba Report Lab Hoja Segunda')

        canvas.restoreState()


class MODELO_01(MODELO):
    '''Definimos las características del modelo base.'''

    def __init__(self):
        '''Inicializamos el modelo.'''

        #~
        #~  T A B L A S
        #~

        self.TIPOTABLA_MODERNA = TableStyle([
            ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
            ('TOPPADDING', (0, 0), (-1, -1), 1),
            ('LEFTPADDING', (0, 0), (-1, -1), 3),
            ('RIGHTPADDING', (0, 0), (-1, -1), 3),
            ('FONT', (0, 0), (-1, -1), MODELO.FUENTE, 8),
            ('GRID', (0, 0), (-1, -1), 0.01 * cm, 'Black'),
            ('FONT', (0, 0), (0, -1), MODELO.FUENTE, 15),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('ALIGN', (0, 0), (0, -1), 'RIGHT'),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('SPAN', (0, 0), (0, -1)),
            ('REPEAROWS', (0, 0), (1, -1)), ])

        self.TIPOTABLA_LIMPIA = TableStyle([
            ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
            ('TOPPADDING', (0, 0), (-1, -1), 1),
            ('LEFTPADDING', (0, 0), (-1, -1), 3),
            ('RIGHTPADDING', (0, 0), (-1, -1), 3),
            ('TEXTCOLOR', (0, 0), (-1, -1), 'Grey'),
            ('FONT', (0, 0), (-1, -1), MODELO.FUENTE, 10),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('ALIGN', (-1, 0), (-1, -1), 'RIGHT'),
            ('ALIGN', (1, 0), (1, -1), 'CENTER'), ])


        #~
        #~ C R E A M O S   E L   C U E R P O   D E L   M E N S A J E
        #~ Y  A Ñ A D I M O S  T R E S   P A R R A F O S  Y
        #~ D O S   T A B L A S
        #~

        self.CUERPO = []
        PARRAFO_P1 = Paragraph('Este es el texto del parrafo 1' * 50, MODELO.EST_1)
        PARRAFO_P2 = Paragraph('Este es el texto del parrafo 2' * 50, MODELO.EST_2)
        PARRAFO_P3 = Paragraph('Este es el texto del parrafo 3' * 50, MODELO.EST_3)

        self.CUERPO.append(self.PARRAFO_P1)
        self.CUERPO.append(Spacer(0, 1 * cm))
        self.CUERPO.append(self.PARRAFO_P2)
        self.CUERPO.append(NextPageTemplate('resto'))
        self.CUERPO.append(PageBreak())
        self.CUERPO.append(self.PARRAFO_P3)
        self.CUERPO.append(Spacer(0, 2 * cm))

        DATA_T1 = [
            ['00', '10', '20', '30', '...'],
            ['01', '11', '21', '...', '...'],
            ['02', '12', '...', '...', '-1-4'],
            ['03', '...', '...', '-2-3', '-1-3'],
            ['...', '...', '-3-2', '-2-2', '-1-2'],
            ['...', '-4-1', '-3-1', '-2-1', '-1-1'], ]

        TABLA_T1 = Table(DATA_T1, style = self.TIPOTABLA_LIMPIA)

        self.CUERPO.append(TABLA_T1)

        self.CUERPO.append(Spacer(0, 2 * cm))

        DATA_T2 = [
            ['Hola', 'Hola', 'Hola', 'Hola', 'Hola', 'Hola', 'Hola', ],
            ['Hola', 'Hola', 'Hola', 'Hola', 'Hola', 'Hola', 'Hola', ],
            ['Hola', 'Hola', 'Hola', 'Hola', 'Hola', 'Hola', 'Hola', ],
            ['Hola', 'Hola', 'Hola', 'Hola', 'Hola', 'Hola', 'Hola', ],
            ['Hola', 'Hola', 'Hola', 'Hola', 'Hola', 'Hola', 'Hola', ],
            ['Hola', 'Hola', 'Hola', 'Hola', 'Hola', 'Hola', 'Hola', ], ]

        TABLA_T2 = Table(DATA_T2, style = self.TIPOTABLA_MODERNA)

        self.CUERPO.append(TABLA_T2)

    def construir_pdf(self):
        '''Lanzamos el código.'''

        MODELO.HOJA_MODERNA.build(self.CUERPO)
        # Lanzar un visor de pdf
        # os.startfile(NOMBRE_FICHERO)
        pass


if __name__ == '__main__':
    TEST = MODELO_01()
    # print TEST.__dict__
    # print dir(TEST)
    TEST.construir_pdf()
