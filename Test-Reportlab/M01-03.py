#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
http://elviajedelnavegante.blogspot.com/2010/03/crear-documentos-pdf-en-python-y-1.html
http://elviajedelnavegante.blogspot.com/2010/03/crear-documentos-pdf-en-python-y-2.html
http://elviajedelnavegante.blogspot.com/2010/04/crear-documentos-pdf-en-python-y-3.html

[...]

En primer lugar vamos a ver lo que es PLATYPUS (Page Layout and Typography Using Scripts).

Con PLATYPUS se pueden diseñar páginas y tipografías utilizando scripts. Con esta herramienta se busca separar las decisiones de diseño del contenido del documento, tanto como sea posible. Es decir, es una especie de formateador de texto, en donde se formatea el diseño del texto, de manera que si queremos cambiar la apariencia del texto solo cambiaremos el diseño, sin tener que cambiar nada en el texto.

Los párrafos de texto son construidos utilizando estilos de párrafos y las páginas se construyen usando plantillas (templates) de páginas, con la intención de que cientos de documentos de miles de páginas puedan ser reformateadas de diferentes estilos con unas pocas líneas en un único fichero el cual contiene los estilos de párrafos y las especificaciones del diseño de la página. Un símil podría ser una página HTML y el diseño que se le da mediante una hola CSS.

PLATYPUS está pensado para hacer un diseño por capas, de arriba hacia abajo. Dichas capas podemos verlas a continuación:

   1. DocTemplates - La plantilla del documento. El contenedor último de un documento.
   2. PageTemplates - Las especificaciones para diseñar páginas de varias clases.
   3. Frames - Las especificaciones de regiones en la páginas que pueden contener texto ó gráficos.
   4. Flowables - Elementos de texto ó gráficos que están incrustados en el documento (párrafos, tablas, imágenes, pero no pies de página, por ejemplo).
   5. pdfgen.Canvas - El nivel más bajo que revice las órdenes de pintar en el documento desde las otras capas. Este nivel es el que hemos estado utilizando en los post anteriores.

El DocTemplates contiene uno ó más PageTemplates y cada uno de ellos a su vez puede contener uno ó más Frames. Los Flowables son elementos que pueden estar incluidos en un Frame (por ejemplo, un párrafo ó una tabla).

[...]

'''

import os

from reportlab.lib import colors
from reportlab.lib.pagesizes import A3
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.pdfmetrics import registerFontFamily
from reportlab.pdfbase.ttfonts import TTFont
#from reportlab.platypus.doctemplate import ActionFlowable
#from reportlab.platypus.doctemplate import BaseDocTemplate
#from reportlab.platypus.doctemplate import FrameBreak
#from reportlab.platypus.doctemplate import Indenter
#from reportlab.platypus.doctemplate import NextPageTemplate
#from reportlab.platypus.doctemplate import NotAtTopPageBreak
#from reportlab.platypus.doctemplate import PageBegin
#from reportlab.platypus.doctemplate import PageTemplate
from reportlab.platypus.doctemplate import SimpleDocTemplate
#from reportlab.platypus.flowables import KeepTogether
from reportlab.platypus import Image
from reportlab.platypus import Paragraph
#from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Spacer
from reportlab.platypus import Table

'''
--> Ver los nº's con FontMatrix
>>> print unichr(0x25a1)
□
>>> print unichr(0x2611)
☑
>>> print unichr(0x2612)
☒
>>> print unichr(0x2713)
✓
>>> print unichr(0x2717)
✗
'''
CKB = unichr(0x25a1)
CKB_YES = unichr(0x2611)
CKB_NO = unichr(0x2612)

PAPEL = A4
WIDTH, HEIGHT = PAPEL
PAGE_HEIGHT = PAPEL[1]
PAGE_WIDTH = PAPEL[0]
TITULO = 'MODELO 1 - INFORMACIÓN GENERAL'
AUTOR = 'Luis Cabrera Sauco'
TEMA = 'Modelo 1 - APPCC'
KEYWORDS = 'palabras clave en este documento'
PRODUCER = AUTOR
NOMBRE_DOCUMENTO = 'APPCC-MODELO_01.pdf'
IMAGEN = '/home/lcabrera/Imágenes/CAFETERIA/Printer.Ticket.Logo.NUEVO_192x92.png'

LEFTMARGIN = 1 * cm
RIGHTMARGIN = 1 * cm
TOPMARGIN = 1 * cm
BOTTONMARGIN = 1 * cm

COLOR_FONDO_CABECERA_1 = colors.blueviolet
COLOR_TEXTO_CABECERA_1 = colors.white

COLOR_FONDO_CABECERA_2 = colors.cadetblue
COLOR_TEXTO_CABECERA_2 = colors.black

COLOR_FONDO_CABECERA_3 = colors.gray
COLOR_TEXTO_CABECERA_3 = colors.white

ESTILO_GENERAL = [
    ('BOX', (0, 0), (-1, -1), 1.0, colors.black),
    ('GRID', (0, 0), (-1, -1), 1.0, colors.black),
    ('BACKGROUND', (0, 0), (-1, -1), colors.transparent),
    ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
    ('FONTSIZE', (0, 0), (-1, -1), 10),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('LEFTPADDING', (0, 0), (-1, -1), 3),
    ('RIGHTPADDING', (0, 0), (-1, -1), 3),
]

# DATOS DEL FORMULARIO
FECHA = '15/04/2011'
RAZON_SOCIAL = 'C.I.F.: 43.658183C'
NOMBRE_COMERCIAL = 'Cafetería Boliche'
DIRECCION = 'Avda. José Mesa y López, 76, local 3 - 35010, Las Palmas de Gran Canaria.'
#DIRECCION = 'Direccion'
TELEFONO1 = '+34 828 028 401'
FAX = ''
EMAIL = 'cafeteriaboliche@gmail.com'

# Gente que forma el equipo de autocontrol:
CKB_SOLO_PERSONAL = 1
if CKB_SOLO_PERSONAL == 1:
    CKB_SOLO_PERSONAL = CKB_YES
else:
    CKB_SOLO_PERSONAL = CKB

CKB_MIXTO = 0
if CKB_MIXTO == 1:
    CKB_MIXTO = CKB_YES
else:
    CKB_MIXTO = CKB

# TODO: REVISAR ESTA CHAPUZA (Diccionario)
EQUIPO_AUTOCONTROL = {}
nombre = 'Luis Cabrera Sauco'
cargo = 'Propietario'
EQUIPO_AUTOCONTROL[nombre] = cargo
nombre = 'Pedro Ricardo Cabrera Sauco'
cargo = 'Encargado'
EQUIPO_AUTOCONTROL[nombre] = cargo
#------------------------------------------

NOMBRE_RESPONSABLE_AUTOCONTROL = 'Luis Cabrera Sauco - Propietario'
NOMBRE_RESPONSABLE_AUTOCONTROL_EMPRESA = 'Pedro Ricardo Cabrera Sauco - Encargado'

NUMERO_TRABAJADORES = 1
if NUMERO_TRABAJADORES <= 10:
    CKB_NUMERO_TRABAJADORES_10 = CKB_YES
    CKB_NUMERO_TRABAJADORES_49 = CKB
    CKB_NUMERO_TRABAJADORES_50 = CKB
elif NUMERO_TRABAJADORES > 50:
    CKB_NUMERO_TRABAJADORES_10 = CKB
    CKB_NUMERO_TRABAJADORES_49 = CKB
    CKB_NUMERO_TRABAJADORES_50 = CKB_YES
else:
    CKB_NUMERO_TRABAJADORES_10 = CKB
    CKB_NUMERO_TRABAJADORES_49 = CKB_YES
    CKB_NUMERO_TRABAJADORES_50 = CKB

NUMERO_MANIPULADORES = 1

NUMERO_COMIDAS_DIA = 0
if NUMERO_COMIDAS_DIA <= 50:
    CKB_COMIDAS_MENOS_50 = CKB_YES
    CKB_COMIDAS_ENTRE_51_Y_150 = CKB
    CKB_COMIDAS_ENTRE_151_Y_500 = CKB
    CKB_COMIDAS_ENTRE_501_Y_1000 = CKB
    CKB_COMIDAS_MAS_1000 = CKB
elif NUMERO_COMIDAS_DIA < 151 and NUMERO_COMIDAS_DIA > 50:
    CKB_COMIDAS_MENOS_50 = CKB
    CKB_COMIDAS_ENTRE_51_Y_150 = CKB_YES
    CKB_COMIDAS_ENTRE_151_Y_500 = CKB
    CKB_COMIDAS_ENTRE_501_Y_1000 = CKB
    CKB_COMIDAS_MAS_1000 = CKB
elif NUMERO_COMIDAS_DIA < 501 and NUMERO_COMIDAS_DIA > 150:
    CKB_COMIDAS_MENOS_50 = CKB
    CKB_COMIDAS_ENTRE_51_Y_150 = CKB
    CKB_COMIDAS_ENTRE_151_Y_500 = CKB_YES
    CKB_COMIDAS_ENTRE_501_Y_1000 = CKB
    CKB_COMIDAS_MAS_1000 = CKB
elif NUMERO_COMIDAS_DIA < 1001 and NUMERO_COMIDAS_DIA > 500:
    CKB_COMIDAS_MENOS_50 = CKB
    CKB_COMIDAS_ENTRE_51_Y_150 = CKB
    CKB_COMIDAS_ENTRE_151_Y_500 = CKB
    CKB_COMIDAS_ENTRE_501_Y_1000 = CKB_YES
    CKB_COMIDAS_MAS_1000 = CKB
else:
    CKB_COMIDAS_MENOS_50 = CKB
    CKB_COMIDAS_ENTRE_51_Y_150 = CKB
    CKB_COMIDAS_ENTRE_151_Y_500 = CKB
    CKB_COMIDAS_ENTRE_501_Y_1000 = CKB
    CKB_COMIDAS_MAS_1000 = CKB_YES

# Sector empresarial:
#    1 - Restauración social
#    2 - Restauración comercial
#    3 - Venta minorista de comidas preparadas
SECTOR_EMPRESARIAL = 2
if SECTOR_EMPRESARIAL == 1:
    CKB_SECTOR_1 = CKB_YES
    CKB_SECTOR_2 = CKB
    CKB_SECTOR_3 = CKB
elif SECTOR_EMPRESARIAL == 2:
    CKB_SECTOR_1 = CKB
    CKB_SECTOR_2 = CKB_YES
    CKB_SECTOR_3 = CKB
elif SECTOR_EMPRESARIAL == 3:
    CKB_SECTOR_1 = CKB
    CKB_SECTOR_2 = CKB
    CKB_SECTOR_3 = CKB_YES
else:
    print 'Sector empresarial no permitido'

# Si se optó por Restauración social en el punto anterior, estas
# son las opciones:
#    1A - Colegio
#    1B - Esc. Infantil
#    1C - Residencia 3º edad
#    1D - Hospital
#    1E - Empresa
#    1F - Otros
#    1FA - TextoOtros
# Si se optó por Restauración comercial, estas son las opciones:
#    2A - Restaurante
#    2B - Bar/cafetería
#    2C - Establecimiento de temporada
#    2D - Establecimiento comida para llevar
#    2E - Otros
#    2EA - TextoOtros
ESPECIALIDAD_SECTOR_EMPRESARIAL = '2B'
ESPECIALIDAD_SECTOR_EMPRESARIAL_OTROS = 'Texto de ejemplo para un campo otros.'
CKB_SECTOR_1FA = ''
CKB_SECTOR_2EA = ''

if ESPECIALIDAD_SECTOR_EMPRESARIAL == '1A':
    CKB_SECTOR_1A = CKB_YES
    CKB_SECTOR_1B = CKB
    CKB_SECTOR_1C = CKB
    CKB_SECTOR_1D = CKB
    CKB_SECTOR_1E = CKB
    CKB_SECTOR_1F = CKB
    CKB_SECTOR_2A = CKB
    CKB_SECTOR_2B = CKB
    CKB_SECTOR_2C = CKB
    CKB_SECTOR_2D = CKB
    CKB_SECTOR_2E = CKB
elif ESPECIALIDAD_SECTOR_EMPRESARIAL == '1B':
    CKB_SECTOR_1A = CKB
    CKB_SECTOR_1B = CKB_YES
    CKB_SECTOR_1C = CKB
    CKB_SECTOR_1D = CKB
    CKB_SECTOR_1E = CKB
    CKB_SECTOR_1F = CKB
    CKB_SECTOR_2A = CKB
    CKB_SECTOR_2B = CKB
    CKB_SECTOR_2C = CKB
    CKB_SECTOR_2D = CKB
    CKB_SECTOR_2E = CKB
elif ESPECIALIDAD_SECTOR_EMPRESARIAL == '1C':
    CKB_SECTOR_1A = CKB
    CKB_SECTOR_1B = CKB
    CKB_SECTOR_1C = CKB_YES
    CKB_SECTOR_1D = CKB
    CKB_SECTOR_1E = CKB
    CKB_SECTOR_1F = CKB
    CKB_SECTOR_2A = CKB
    CKB_SECTOR_2B = CKB
    CKB_SECTOR_2C = CKB
    CKB_SECTOR_2D = CKB
    CKB_SECTOR_2E = CKB
elif ESPECIALIDAD_SECTOR_EMPRESARIAL == '1D':
    CKB_SECTOR_1A = CKB
    CKB_SECTOR_1B = CKB
    CKB_SECTOR_1C = CKB
    CKB_SECTOR_1D = CKB_YES
    CKB_SECTOR_1E = CKB
    CKB_SECTOR_1F = CKB
    CKB_SECTOR_2A = CKB
    CKB_SECTOR_2B = CKB
    CKB_SECTOR_2C = CKB
    CKB_SECTOR_2D = CKB
    CKB_SECTOR_2E = CKB
elif ESPECIALIDAD_SECTOR_EMPRESARIAL == '1E':
    CKB_SECTOR_1A = CKB
    CKB_SECTOR_1B = CKB
    CKB_SECTOR_1C = CKB
    CKB_SECTOR_1D = CKB
    CKB_SECTOR_1E = CKB_YES
    CKB_SECTOR_1F = CKB
    CKB_SECTOR_2A = CKB
    CKB_SECTOR_2B = CKB
    CKB_SECTOR_2C = CKB
    CKB_SECTOR_2D = CKB
    CKB_SECTOR_2E = CKB
elif ESPECIALIDAD_SECTOR_EMPRESARIAL == '1F':
    # Verificamos el campo otros:
    if ESPECIALIDAD_SECTOR_EMPRESARIAL_OTROS <> '':
        CKB_SECTOR_1FA = ESPECIALIDAD_SECTOR_EMPRESARIAL_OTROS
    else:
        CKB_SECTOR_1FA = ''
    CKB_SECTOR_1A = CKB
    CKB_SECTOR_1B = CKB
    CKB_SECTOR_1C = CKB
    CKB_SECTOR_1D = CKB
    CKB_SECTOR_1E = CKB
    CKB_SECTOR_1F = CKB_YES
    CKB_SECTOR_2A = CKB
    CKB_SECTOR_2B = CKB
    CKB_SECTOR_2C = CKB
    CKB_SECTOR_2D = CKB
    CKB_SECTOR_2E = CKB
elif ESPECIALIDAD_SECTOR_EMPRESARIAL == '2A':
    CKB_SECTOR_1A = CKB
    CKB_SECTOR_1B = CKB
    CKB_SECTOR_1C = CKB
    CKB_SECTOR_1D = CKB
    CKB_SECTOR_1E = CKB
    CKB_SECTOR_1F = CKB
    CKB_SECTOR_2A = CKB_YES
    CKB_SECTOR_2B = CKB
    CKB_SECTOR_2C = CKB
    CKB_SECTOR_2D = CKB
    CKB_SECTOR_2E = CKB
elif ESPECIALIDAD_SECTOR_EMPRESARIAL == '2B':
    CKB_SECTOR_1A = CKB
    CKB_SECTOR_1B = CKB
    CKB_SECTOR_1C = CKB
    CKB_SECTOR_1D = CKB
    CKB_SECTOR_1E = CKB
    CKB_SECTOR_1F = CKB
    CKB_SECTOR_2A = CKB
    CKB_SECTOR_2B = CKB_YES
    CKB_SECTOR_2C = CKB
    CKB_SECTOR_2D = CKB
    CKB_SECTOR_2E = CKB
elif ESPECIALIDAD_SECTOR_EMPRESARIAL == '2C':
    CKB_SECTOR_1A = CKB
    CKB_SECTOR_1B = CKB
    CKB_SECTOR_1C = CKB
    CKB_SECTOR_1D = CKB
    CKB_SECTOR_1E = CKB
    CKB_SECTOR_1F = CKB
    CKB_SECTOR_2A = CKB
    CKB_SECTOR_2B = CKB
    CKB_SECTOR_2C = CKB_YES
    CKB_SECTOR_2D = CKB
    CKB_SECTOR_2E = CKB
elif ESPECIALIDAD_SECTOR_EMPRESARIAL == '2D':
    CKB_SECTOR_1A = CKB
    CKB_SECTOR_1B = CKB
    CKB_SECTOR_1C = CKB
    CKB_SECTOR_1D = CKB
    CKB_SECTOR_1E = CKB
    CKB_SECTOR_1F = CKB
    CKB_SECTOR_2A = CKB
    CKB_SECTOR_2B = CKB
    CKB_SECTOR_2C = CKB
    CKB_SECTOR_2D = CKB_YES
    CKB_SECTOR_2E = CKB
elif ESPECIALIDAD_SECTOR_EMPRESARIAL == '2E':
    # Verificamos el campo otros:
    if ESPECIALIDAD_SECTOR_EMPRESARIAL_OTROS <> '':
        CKB_SECTOR_2EA = ESPECIALIDAD_SECTOR_EMPRESARIAL_OTROS
    else:
        CKB_SECTOR_2EA = ''
    CKB_SECTOR_1A = CKB
    CKB_SECTOR_1B = CKB
    CKB_SECTOR_1C = CKB
    CKB_SECTOR_1D = CKB
    CKB_SECTOR_1E = CKB
    CKB_SECTOR_1F = CKB
    CKB_SECTOR_2A = CKB
    CKB_SECTOR_2B = CKB
    CKB_SECTOR_2C = CKB
    CKB_SECTOR_2D = CKB
    CKB_SECTOR_2E = CKB_YES
else:
    print 'Especialidad, dentro del sector empresarial, no permitido'

# Después de su elaboración las comidas van a ser consumidas:
#   1 - Inmediatamente
#   2 - Después de un periodo de conservación en caliente
#   3 - Después de recalentar
#   4 - Después de un periodo de conservación en frío
#   5 - Después de realizar un procesado adicional
#       ejemplo: fritura en precocinados)
PERIODO_CONSUMO = '3'

if PERIODO_CONSUMO == '1':
    CKB_USO_1A = CKB_YES
    CKB_USO_1B = CKB
    CKB_USO_1C = CKB
    CKB_USO_1D = CKB
    CKB_USO_1E = CKB
elif PERIODO_CONSUMO == '2':
    CKB_USO_1A = CKB
    CKB_USO_1B = CKB_YES
    CKB_USO_1C = CKB
    CKB_USO_1D = CKB
    CKB_USO_1E = CKB
elif PERIODO_CONSUMO == '3':
    CKB_USO_1A = CKB
    CKB_USO_1B = CKB
    CKB_USO_1C = CKB_YES
    CKB_USO_1D = CKB
    CKB_USO_1E = CKB
elif PERIODO_CONSUMO == '4':
    CKB_USO_1A = CKB
    CKB_USO_1B = CKB
    CKB_USO_1C = CKB
    CKB_USO_1D = CKB_YES
    CKB_USO_1E = CKB
elif PERIODO_CONSUMO == '5':
    CKB_USO_1A = CKB
    CKB_USO_1B = CKB
    CKB_USO_1C = CKB
    CKB_USO_1D = CKB
    CKB_USO_1E = CKB_YES
else:
    print 'Su elección no es correcta.'



# Las comidas elaboradas en el establecimiento van a ser consumidas en:
#   1 - El propio establecimiento
#   2 - En otro establecimiento de comidas preparadas
#   3 - En un domicilio particular realizándose reparto a domicilio
#   4 - En un domicilio particular sin reparto a domicilio
#   5 - Otros(indicar cual):
DONDE_SE_CONSUME = '1'
DONDE_SE_CONSUME_OTROS = ''
CKB_USO_2E1 = ''

if DONDE_SE_CONSUME == '1':
    CKB_USO_2A = CKB_YES
    CKB_USO_2B = CKB
    CKB_USO_2C = CKB
    CKB_USO_2D = CKB
    CKB_USO_2E = CKB
elif DONDE_SE_CONSUME == '2':
    CKB_USO_2A = CKB
    CKB_USO_2B = CKB_YES
    CKB_USO_2C = CKB
    CKB_USO_2D = CKB
    CKB_USO_2E = CKB
elif DONDE_SE_CONSUME == '3':
    CKB_USO_2A = CKB
    CKB_USO_2B = CKB
    CKB_USO_2C = CKB_YES
    CKB_USO_2D = CKB
    CKB_USO_2E = CKB
elif DONDE_SE_CONSUME == '4':
    CKB_USO_2A = CKB
    CKB_USO_2B = CKB
    CKB_USO_2C = CKB
    CKB_USO_2D = CKB_YES
    CKB_USO_2E = CKB
elif DONDE_SE_CONSUME == '5':
    CKB_USO_2A = CKB
    CKB_USO_2B = CKB
    CKB_USO_2C = CKB
    CKB_USO_2D = CKB
    CKB_USO_2E = CKB_YES
    if DONDE_SE_CONSUME_OTROS <> '':
        CKB_USO_2E1 = DONDE_SE_CONSUME_OTROS
    else:
        CKB_USO_2E1 = ''
else:
    print 'Opción no contemplada.'

# 4. POBLACIÓN DESTINO:
# Las comidas elaboradas en el establecimiento van destinadas específicamente a:
#   1 - Población en general
#   2 - Población de riesgo (niños, ancianos, enfermos, embarazadas, alérgicos/intolerantes)
#   3 - Ambos
PERFIL_CONSUMIDOR = '1'

if PERFIL_CONSUMIDOR == '1':
    CKB_PERFIL_1 = CKB_YES
    CKB_PERFIL_2 = CKB
    CKB_PERFIL_3 = CKB
elif PERFIL_CONSUMIDOR == '2':
    CKB_PERFIL_1 = CKB
    CKB_PERFIL_2 = CKB_YES
    CKB_PERFIL_3 = CKB
elif PERFIL_CONSUMIDOR == '3':
    CKB_PERFIL_1 = CKB
    CKB_PERFIL_2 = CKB
    CKB_PERFIL_3 = CKB_YES
else:
    print 'Opción no contemplada.'



# Registrar Fuentes:
pdfmetrics.registerFont(TTFont('OpenSymbol', '/usr/share/fonts/truetype/openoffice/opens___.ttf'))

# Creamos un PageTemplate de ejemplo.
estiloHoja = getSampleStyleSheet()

# Inicializamos la lista Platypus Story.
story = []

# COMENZAMOS A DEFINIR LA CABECERA:
# Definimos cómo queremos que sea el estilo de la PageTemplate.
cabecera = estiloHoja['Heading1']
cabecera.pageBreakBefore = 0
cabecera.allowWidows = 1
cabecera.backColor = colors.silver
cabecera.borderColor = colors.black
cabecera.borderPadding = 15
cabecera.borderRadius = 10
cabecera.borderWidth = 2
cabecera.fontSize = 18
cabecera.keepWithNext = 0

# Incluimos un Flowable, que en este caso es un párrafo.
parrafo = Paragraph(TITULO, cabecera)

# Y para finalizar la cabecera, lo incluimos en el Platypus story.
story.append(parrafo)

# Dejamos espacio. (Si no lo incluimos, no sale)
story.append(Spacer(0, 20))

# Ahora incluimos una imagen.
#fichero_imagen = IMAGEN
#imagen_logo = Image(os.path.realpath(fichero_imagen), width=192, height=92)

# Y lo incluimos en el story. (Si no lo incluimos, no sale)
#story.append(imagen_logo)

# Dejamos algo de espacio: (Si no lo incluimos, no sale)
#story.append(Spacer(0, 20))
###############################################################################

# Comenzamos definiendo los datos
M01_T00_L00 = [TITULO, '', '', '']
M01_T00_L01 = ['Fecha: ' + FECHA, '', 'Edición: ' + AUTOR, '']
M01_T00_L02 = ['', '', '', '']

# Ahora los unificamos en una sola variable, por comodidad:
M01_T00_DATA = [M01_T00_L00, M01_T00_L01, M01_T00_L02]

# Definimos las características de la tabla
M01_T00 = Table(M01_T00_DATA, colWidths=((PAGE_WIDTH - (LEFTMARGIN + RIGHTMARGIN)) / 4), splitByRow=1, repeatRows=1)

# Añadimos el estilo general:
M01_T00.setStyle(ESTILO_GENERAL)

# Ahora, añadimos los estilos particulares de cada tabla:
M01_T00.setStyle([
    # Primera fila: Encabezado del formulario
    ('SPAN', (0, 0), (3, 0)),
    ('BACKGROUND', (0, 0), (3, 0), COLOR_FONDO_CABECERA_1),
    ('TEXTCOLOR', (0, 0), (3, 0), COLOR_TEXTO_CABECERA_1),
    ('FONTNAME', (0, 0), (3, 0), 'Times-Bold'),
    ('FONTSIZE', (0, 0), (3, 0), 14),
    ('ALIGN', (0, 0), (3, 0), 'CENTER'),

    # Segunda línea, primer grupo:
    ('SPAN', (0, 1), (1, 1)),
    ('BACKGROUND', (0, 1), (1, 1), COLOR_FONDO_CABECERA_2),
    ('TEXTCOLOR', (0, 1), (1, 1), COLOR_TEXTO_CABECERA_2),
    ('FONTNAME', (0, 1), (1, 1), 'Helvetica'),
    ('FONTSIZE', (0, 1), (1, 1), 12),

    # Segunda línea, segundo grupo:
    ('SPAN', (2, 1), (3, 1)),
    ('BACKGROUND', (2, 1), (3, 1), COLOR_FONDO_CABECERA_2),
    ('TEXTCOLOR', (2, 1), (3, 1), COLOR_TEXTO_CABECERA_2),
    ('FONTNAME', (2, 1), (3, 1), 'Helvetica'),
    ('FONTSIZE', (2, 1), (3, 1), 12),

    # Tercera línea: un separador:
    ('SPAN', (0, 2), (3, 2)),

    ])

# Añadimos la tabla al workflow de la página:
story.append(M01_T00)

# Por último, añadimos un separador:
story.append(Spacer(0, 5))

###############################################################################

# Comenzamos definiendo los datos
M01_T01_L00 = ['1. INFORMACIÓN BÁSICA']
M01_T01_L01 = ['Razón Social: ' + RAZON_SOCIAL]
M01_T01_L02 = ['Nombre comercial: ' + NOMBRE_COMERCIAL]
M01_T01_L03 = ['Dirección: ' + DIRECCION, ]
M01_T01_L04 = ['Teléfono.: ' + TELEFONO1, '', 'Fax: ' + FAX, '']
M01_T01_L05 = ['Correo electrónico: ' + EMAIL]

# Ahora los unificamos en una sola variable, por comodidad:
M01_T01_DATA = [
    M01_T01_L00, M01_T01_L01, M01_T01_L02, M01_T01_L03, M01_T01_L04, M01_T01_L05, ]

# Definimos las características de la tabla
M01_T01 = Table(M01_T01_DATA, colWidths=((PAGE_WIDTH - (LEFTMARGIN + RIGHTMARGIN)) / 4), splitByRow=1, repeatRows=1)

# Añadimos el estilo general:
M01_T01.setStyle(ESTILO_GENERAL)

# Ahora, añadimos los estilos particulares de cada tabla:
M01_T01.setStyle([
    # Información Básica:
    ('SPAN', (0, 0), (3, 0)),
    ('BACKGROUND', (0, 0), (3, 0), COLOR_FONDO_CABECERA_3),
    ('TEXTCOLOR', (0, 0), (3, 0), COLOR_TEXTO_CABECERA_3),
    ('FONTNAME', (0, 0), (3, 0), 'Helvetica'),
    ('FONTSIZE', (0, 0), (3, 0), 11),

    # Razón Social:
    ('SPAN', (0, 1), (3, 1)),
    # Nombre Comercial:
    ('SPAN', (0, 2), (3, 2)),
    # Dirección:
    ('SPAN', (0, 3), (3, 3)),
    # Teléfono:
    ('SPAN', (0, 4), (1, 4)),
    # Fax:
    ('SPAN', (2, 4), (3, 4)),
    # eMail:
    ('SPAN', (0, 5), (3, 5)), ])

# Añadimos la tabla al workflow de la página:
story.append(M01_T01)

# Por último, añadimos un separador:
story.append(Spacer(0, 5))

###############################################################################

# Comenzamos definiendo los datos
M01_T02_L00 = ['2. ACTIVIDADES', '', '', '']
M01_T02_L01 = ['Equipo de trabajo de autocontrol formado por:', '', '', '']
M01_T02_L02 = [CKB_SOLO_PERSONAL, ' Sólo por personal del establecimiento', '', '']
M01_T02_L03 = [CKB_MIXTO, ' Equipo mixto, personal establecimiento y empresa externa', '', '']
M01_T02_L04 = ['Listado de personas que forman parte del equipo de autocontrol:', '', '', '']
M01_T02_L05 = ['    ' + str(EQUIPO_AUTOCONTROL)]
M01_T02_L06 = ['RESPONSABLE DEL SISTEMA DE AUTOCONTROL (Nombre y cargo): ', '', '', '']
M01_T02_L07 = ['    ' + str(NOMBRE_RESPONSABLE_AUTOCONTROL)]
M01_T02_L08 = ['RESPONSABLE DE LA EMPRESA (Nombre y cargo):', '', '', '']
M01_T02_L09 = ['    ' + str(NOMBRE_RESPONSABLE_AUTOCONTROL_EMPRESA)]
M01_T02_L10 = ['Firma del responsable de la empresa:\n\n', '']
M01_T02_L11 = ['Número de trabajadores:', '', '', '']
M01_T02_L12 = [CKB_NUMERO_TRABAJADORES_10, ' Menos de 10', '', '']
M01_T02_L13 = [CKB_NUMERO_TRABAJADORES_49, ' Entre 10 y 49', '', '']
M01_T02_L14 = [CKB_NUMERO_TRABAJADORES_50, ' 50 o más', '', '']
M01_T02_L15 = ['Nº de manipuladores: ', NUMERO_MANIPULADORES]
M01_T02_L16 = ['Número de comidas preparadas diariamente:', '', '', '']
M01_T02_L17 = [CKB_COMIDAS_MENOS_50, ' Menos de 50', '', '']
M01_T02_L18 = [CKB_COMIDAS_ENTRE_51_Y_150, ' Entre 51 y 150', '', '']
M01_T02_L19 = [CKB_COMIDAS_ENTRE_151_Y_500, ' Entre 151 y 500', '', '']
M01_T02_L20 = [CKB_COMIDAS_ENTRE_501_Y_1000, ' Entre 501 y 1000', '', '']
M01_T02_L21 = [CKB_COMIDAS_MAS_1000, ' Más de 1000', '', '']
M01_T02_L22 = ['Sector:', '', '', '']
M01_T02_L23 = [CKB_SECTOR_1, ' Restauración social:', '', '']
M01_T02_L24 = [  CKB_SECTOR_1A, '111', ' Colegio', '333']
M01_T02_L25 = [  CKB_SECTOR_1B, '111', ' Esc. Infantil', '']
M01_T02_L26 = [  CKB_SECTOR_1C, '111', ' Residencia 3º edad', '']
M01_T02_L27 = [  CKB_SECTOR_1D, '111', ' Hospital', '']
M01_T02_L28 = [  CKB_SECTOR_1E, '111', ' Empresa', '']
M01_T02_L29 = [  CKB_SECTOR_1F, '111', ' Otros (Indicar cuál): ' + CKB_SECTOR_1FA]
M01_T02_L30 = [CKB_SECTOR_2, ' Restauración comercial:', '', '']
M01_T02_L31 = [  CKB_SECTOR_2A, '111', ' Restaurante', '']
M01_T02_L32 = [  CKB_SECTOR_2B, '111', ' Bar/cafetería', '']
M01_T02_L33 = [  CKB_SECTOR_2C, '111', ' Establecimiento de temporada', '']
M01_T02_L34 = [  CKB_SECTOR_2D, '111', ' Establecimiento comida para llevar', '']
M01_T02_L35 = [  CKB_SECTOR_2E, '111', ' Otros (Indicar cuál): ', CKB_SECTOR_2EA]
M01_T02_L36 = [CKB_SECTOR_3, ' Venta minorista de comidas preparadas: ', '', '']

# Ahora los unificamos en una sola variable, por comodidad:
M01_T02_DATA = [
    M01_T02_L00, M01_T02_L01, M01_T02_L02, M01_T02_L03, M01_T02_L04, M01_T02_L05, M01_T02_L06, M01_T02_L07, M01_T02_L08, M01_T02_L09,
    M01_T02_L10, M01_T02_L11, M01_T02_L12, M01_T02_L13, M01_T02_L14, M01_T02_L15, M01_T02_L16, M01_T02_L17, M01_T02_L18, M01_T02_L19,
    M01_T02_L20, M01_T02_L21, M01_T02_L22, M01_T02_L23, M01_T02_L24, M01_T02_L25, M01_T02_L26, M01_T02_L27, M01_T02_L28, M01_T02_L29,
    M01_T02_L30, M01_T02_L31, M01_T02_L32, M01_T02_L33, M01_T02_L34, M01_T02_L35, M01_T02_L36, ]

# Definimos las características de la tabla
M01_T02 = Table(M01_T02_DATA, colWidths=((PAGE_WIDTH - (LEFTMARGIN + RIGHTMARGIN)) / 4), splitByRow=1, repeatRows=1)

# Añadimos el estilo general:
M01_T02.setStyle(ESTILO_GENERAL)

# Ahora, añadimos los estilos particulares de cada tabla:
M01_T02.setStyle([
    # Actividades
    ('SPAN', (0, 0), (3, 0)),
    ('BACKGROUND', (0, 0), (3, 0), COLOR_FONDO_CABECERA_3),
    ('TEXTCOLOR', (0, 0), (3, 0), COLOR_TEXTO_CABECERA_3),
    ('FONTNAME', (0, 0), (3, 0), 'Helvetica'),
    ('FONTSIZE', (0, 0), (3, 0), 11),

    # Equipo formado por:
    ('SPAN', (0, 1), (3, 1)),

    # CKB: Solo personal del establecimiento:
    ('ALIGN', (0, 2), (0, 2), 'RIGHT'),
    ('FONTNAME', (0, 2), (0, 2), 'OpenSymbol'),
    ('SPAN', (1, 2), (3, 2)),

    # Mixto: establecimiento + empresa externa:
    ('ALIGN', (0, 3), (0, 3), 'RIGHT'),
    ('FONTNAME', (0, 3), (0, 3), 'OpenSymbol'),
    ('SPAN', (1, 3), (3, 3)),

    # Listado de personas que forman el equipo de autocontrol:
    ('SPAN', (0, 4), (3, 4)),

    # Listado
    ('SPAN', (0, 5), (3, 5)),

    # Persona responsable del sistema de autocontrol:
    ('SPAN', (0, 6), (3, 6)),

    # Datos de la Persona responsable del sistema de autocontrol:
    ('SPAN', (0, 7), (3, 7)),

    # Persona responsable del sistema de autocontrol, por parte de la empresa:
    ('SPAN', (0, 8), (3, 8)),

    # Datos de la Persona responsable del sistema de autocontrol,
    # por parte de la empresa:
    ('SPAN', (0, 9), (3, 9)),

    # Firma del responsable de la empresa:
    ('SPAN', (0, 10), (1, 10)),
    ('SPAN', (2, 10), (3, 10)),

    # Nº de Trabajadores:
    ('SPAN', (0, 11), (3, 11)),

    # Menos de 10:
    ('ALIGN', (0, 12), (0, 12), 'RIGHT'),
    ('FONTNAME', (0, 12), (0, 12), 'OpenSymbol'),
    ('SPAN', (1, 12), (3, 12)),

    # Entre 10 y 49:
    ('ALIGN', (0, 13), (0, 13), 'RIGHT'),
    ('FONTNAME', (0, 13), (0, 13), 'OpenSymbol'),
    ('SPAN', (1, 13), (3, 13)),

    # 50 ó más:
    ('ALIGN', (0, 14), (0, 14), 'RIGHT'),
    ('FONTNAME', (0, 14), (0, 14), 'OpenSymbol'),
    ('SPAN', (1, 14), (3, 14)),

    # Nº de manipuladores:
    ('SPAN', (1, 15), (3, 15)),

    # Nº de comidas preparadas a diario:
    ('SPAN', (0, 16), (3, 16)),

    # Menos de 50 comidas
    ('ALIGN', (0, 17), (0, 17), 'RIGHT'),
    ('FONTNAME', (0, 17), (0, 17), 'OpenSymbol'),
    ('SPAN', (1, 17), (3, 17)),

    # Entre 51 y 150 comidas diarias
    ('ALIGN', (0, 18), (0, 18), 'RIGHT'),
    ('FONTNAME', (0, 18), (0, 18), 'OpenSymbol'),
    ('SPAN', (1, 18), (3, 18)),

    # Entre 151 y 500 comidas diarias
    ('ALIGN', (0, 19), (0, 19), 'RIGHT'),
    ('FONTNAME', (0, 19), (0, 19), 'OpenSymbol'),
    ('SPAN', (1, 19), (3, 19)),

    # Entre 501 y 1000
    ('ALIGN', (0, 20), (0, 20), 'RIGHT'),
    ('FONTNAME', (0, 20), (0, 20), 'OpenSymbol'),
    ('SPAN', (1, 20), (3, 20)),

    # Más de 1000 comidas al día
    ('ALIGN', (0, 21), (0, 21), 'RIGHT'),
    ('FONTNAME', (0, 21), (0, 21), 'OpenSymbol'),
    ('SPAN', (1, 21), (3, 21)),

    # Sector empresarial
    ('SPAN', (0, 22), (3, 22)),

    # Restauración social
    ('ALIGN', (0, 23), (0, 23), 'RIGHT'),
    ('FONTNAME', (0, 23), (0, 23), 'OpenSymbol'),
    ('SPAN', (1, 23), (3, 23)),

    # Colegios:
    ('SPAN', (0, 24), (1, 24)),
    ('ALIGN', (0, 24), (0, 24), 'RIGHT'),
    ('FONTNAME', (0, 24), (0, 24), 'OpenSymbol'),
    ('SPAN', (2, 24), (3, 24)),

    # Escuelas infantiles:
    ('SPAN', (0, 25), (1, 25)),
    ('ALIGN', (0, 25), (0, 25), 'RIGHT'),
    ('FONTNAME', (0, 25), (0, 25), 'OpenSymbol'),
    ('SPAN', (2, 25), (3, 25)),

    # Residencia 3º edad:
    ('SPAN', (0, 26), (1, 26)),
    ('ALIGN', (0, 26), (0, 26), 'RIGHT'),
    ('FONTNAME', (0, 26), (0, 26), 'OpenSymbol'),
    ('SPAN', (2, 26), (3, 26)),

    # Hospital:
    ('SPAN', (0, 27), (1, 27)),
    ('ALIGN', (0, 27), (0, 27), 'RIGHT'),
    ('FONTNAME', (0, 27), (0, 27), 'OpenSymbol'),
    ('SPAN', (2, 27), (3, 27)),

    # Empresa:
    ('SPAN', (0, 28), (1, 28)),
    ('ALIGN', (0, 28), (0, 28), 'RIGHT'),
    ('FONTNAME', (0, 28), (0, 28), 'OpenSymbol'),
    ('SPAN', (2, 28), (3, 28)),

    # Otros:
    ('SPAN', (0, 29), (1, 29)),
    ('ALIGN', (0, 29), (0, 29), 'RIGHT'),
    ('FONTNAME', (0, 29), (0, 29), 'OpenSymbol'),
    ('SPAN', (2, 29), (3, 29)),

    # Restauración comercial
    ('ALIGN', (0, 30), (0, 30), 'RIGHT'),
    ('FONTNAME', (0, 30), (0, 30), 'OpenSymbol'),
    ('SPAN', (1, 30), (3, 30)),

    # Restaurante:
    ('SPAN', (0, 31), (1, 31)),
    ('ALIGN', (0, 31), (0, 31), 'RIGHT'),
    ('FONTNAME', (0, 31), (0, 31), 'OpenSymbol'),
    ('SPAN', (2, 31), (3, 31)),

    # Bar/cafetería
    ('SPAN', (0, 32), (1, 32)),
    ('ALIGN', (0, 32), (0, 32), 'RIGHT'),
    ('FONTNAME', (0, 32), (0, 32), 'OpenSymbol'),
    ('SPAN', (2, 32), (3, 32)),

    # Establecimiento de temporada
    ('SPAN', (0, 33), (1, 33)),
    ('ALIGN', (0, 33), (0, 33), 'RIGHT'),
    ('FONTNAME', (0, 33), (0, 33), 'OpenSymbol'),
    ('SPAN', (2, 33), (3, 33)),

    # Establecimiento comida para llevar
    ('SPAN', (0, 34), (1, 34)),
    ('ALIGN', (0, 34), (0, 34), 'RIGHT'),
    ('FONTNAME', (0, 34), (0, 34), 'OpenSymbol'),
    ('SPAN', (2, 34), (3, 34)),

    # Otros (Indicar cuál):
    ('SPAN', (0, 35), (1, 35)),
    ('ALIGN', (0, 35), (0, 35), 'RIGHT'),
    ('FONTNAME', (0, 35), (0, 35), 'OpenSymbol'),
    ('SPAN', (2, 35), (3, 35)),

    # Venta minorista de comidas preparadas
    ('ALIGN', (0, 36), (0, 36), 'RIGHT'),
    ('FONTNAME', (0, 36), (0, 36), 'OpenSymbol'),
    ('SPAN', (1, 36), (3, 36)),
])

# Añadimos la tabla al workflow de la página:
story.append(M01_T02)

# Por último, añadimos un separador:
story.append(Spacer(0, 5))

###############################################################################

# Comenzamos definiendo los datos
M01_T03_L00 = ['3. USO ESPERADO:', '', '', '']
M01_T03_L01 = ['Después de su elaboración las comidas van a ser consumidas:', '', '', '']
M01_T03_L02 = [CKB_USO_1A, ' Inmediatamente', '', '']
M01_T03_L03 = [CKB_USO_1B, ' Después de un periodo de conservación en caliente', '', '']
M01_T03_L04 = [CKB_USO_1C, ' Después de recalentar', '', '']
M01_T03_L05 = [CKB_USO_1D, ' Después de un periodo de conservación en frío', '', '']
M01_T03_L06 = [CKB_USO_1E, ' Después de realizar un procesado adicional (ejemplo: fritura en precocinados)', '', '']
M01_T03_L07 = ['Las comidas elaboradas en el establecimiento van a ser consumidas en:', '', '', '']
M01_T03_L08 = [CKB_USO_2A, ' El propio establecimiento', '', '']
M01_T03_L09 = [CKB_USO_2B, ' En otro establecimiento de comidas preparadas', '', '']
M01_T03_L10 = [CKB_USO_2C, ' En un domicilio particular realizándose reparto a domicilio', '', '']
M01_T03_L11 = [CKB_USO_2D, ' En un domicilio particular sin reparto a domicilio', '', '']
M01_T03_L12 = [CKB_USO_2E, ' Otros(indicar cual): ' + CKB_USO_2E1, '', '']

# Ahora los unificamos en una sola variable, por comodidad:
M01_T03_DATA = [
    M01_T03_L00, M01_T03_L01, M01_T03_L02, M01_T03_L03, M01_T03_L04, M01_T03_L05, M01_T03_L06, M01_T03_L07, M01_T03_L08, M01_T03_L09,
    M01_T03_L10, M01_T03_L11, M01_T03_L12, ]

# Definimos las características de la tabla
M01_T03 = Table(M01_T03_DATA, colWidths=((PAGE_WIDTH - (LEFTMARGIN + RIGHTMARGIN)) / 4), splitByRow=1, repeatRows=1)

# Añadimos el estilo general:
M01_T03.setStyle(ESTILO_GENERAL)

# Ahora, añadimos los estilos particulares de cada tabla:
M01_T03.setStyle([

    # USO ESPERADO
    ('SPAN', (0, 0), (3, 0)),
    ('BACKGROUND', (0, 0), (3, 0), COLOR_FONDO_CABECERA_3),
    ('TEXTCOLOR', (0, 0), (3, 0), COLOR_TEXTO_CABECERA_3),
    ('FONTNAME', (0, 0), (3, 0), 'Helvetica'),
    ('FONTSIZE', (0, 0), (3, 0), 11),

    # Despues de su elaboración, las comidas van a ser consumidas:
    ('SPAN', (0, 1), (3, 1)),

    # Inmediatamente
    ('ALIGN', (0, 2), (0, 2), 'RIGHT'),
    ('FONTNAME', (0, 2), (0, 2), 'OpenSymbol'),
    ('SPAN', (1, 2), (3, 2)),

    # Después de un periodo de conservación en caliente:
    ('ALIGN', (0, 3), (0, 3), 'RIGHT'),
    ('FONTNAME', (0, 3), (0, 3), 'OpenSymbol'),
    ('SPAN', (1, 3), (3, 3)),

    # Después de recalentar:
    ('ALIGN', (0, 4), (0, 4), 'RIGHT'),
    ('FONTNAME', (0, 4), (0, 4), 'OpenSymbol'),
    ('SPAN', (1, 4), (3, 4)),

    # Después de un periodo de conservación en frío:
    ('ALIGN', (0, 5), (0, 5), 'RIGHT'),
    ('FONTNAME', (0, 5), (0, 5), 'OpenSymbol'),
    ('SPAN', (1, 5), (3, 5)),

    # Después de realizar un procesado adicional\n(ejemplo: fritura en precocinados):
    ('ALIGN', (0, 6), (0, 6), 'RIGHT'),
    ('FONTNAME', (0, 6), (0, 6), 'OpenSymbol'),
    ('SPAN', (1, 6), (3, 6)),

    # Las comidas elaboradas en el establecimiento van a ser consumidas en:
    ('SPAN', (0, 7), (3, 7)),

    # El propio establecimiento:
    ('ALIGN', (0, 8), (0, 8), 'RIGHT'),
    ('FONTNAME', (0, 8), (0, 8), 'OpenSymbol'),
    ('SPAN', (1, 8), (3, 8)),

    # En otro establecimiento de comidas preparadas:
    ('ALIGN', (0, 9), (0, 9), 'RIGHT'),
    ('FONTNAME', (0, 9), (0, 9), 'OpenSymbol'),
    ('SPAN', (1, 9), (3, 9)),

    # En un domicilio particular realizándose reparto a domicilio:
    ('ALIGN', (0, 10), (0, 10), 'RIGHT'),
    ('FONTNAME', (0, 10), (0, 10), 'OpenSymbol'),
    ('SPAN', (1, 10), (3, 10)),

    # En un domicilio particular sin reparto a domicilio:
    ('ALIGN', (0, 11), (0, 11), 'RIGHT'),
    ('FONTNAME', (0, 11), (0, 11), 'OpenSymbol'),
    ('SPAN', (1, 11), (3, 11)),

    # Otros(indicar cual):
    ('ALIGN', (0, 12), (0, 12), 'RIGHT'),
    ('FONTNAME', (0, 12), (0, 12), 'OpenSymbol'),
    ('SPAN', (1, 12), (3, 12)),

    ])

# Añadimos la tabla al workflow de la página:
story.append(M01_T03)

# Por último, añadimos un separador:
story.append(Spacer(0, 5))

###############################################################################

# Comenzamos definiendo los datos
M01_T04_L00 = ['4. POBLACIÓN DESTINO:', '', '', '']
M01_T04_L01 = ['Las comidas elaboradas en el establecimiento van destinadas específicamente a:', '', '', '']
M01_T04_L02 = [CKB_PERFIL_1, ' Población en general', '', '']
M01_T04_L03 = [CKB_PERFIL_2, ' Población de riesgo (niños, ancianos, enfermos, embarazadas, alérgicos/intolerantes)', '', '']
M01_T04_L04 = [CKB_PERFIL_3, ' Ambos', '', '']

# Ahora los unificamos en una sola variable, por comodidad:
M01_T04_DATA = [
    M01_T04_L00, M01_T04_L01, M01_T04_L02, M01_T04_L03, M01_T04_L04, ]

# Definimos las características de la tabla
M01_T04 = Table(M01_T04_DATA, colWidths=((PAGE_WIDTH - (LEFTMARGIN + RIGHTMARGIN)) / 4), splitByRow=1, repeatRows=1)

# Añadimos el estilo general:
M01_T04.setStyle(ESTILO_GENERAL)

# Ahora, añadimos los estilos particulares de cada tabla:
M01_T04.setStyle([

    # 4. POBLACIÓN DESTINO:
    ('SPAN', (0, 0), (3, 0)),
    ('BACKGROUND', (0, 0), (3, 0), COLOR_FONDO_CABECERA_3),
    ('TEXTCOLOR', (0, 0), (3, 0), COLOR_TEXTO_CABECERA_3),
    ('FONTNAME', (0, 0), (3, 0), 'Helvetica'),
    ('FONTSIZE', (0, 0), (3, 0), 11),

    # Las comidas elaboradas en el establecimiento van destinadas específicamente a:
    ('SPAN', (0, 1), (3, 1)),

    # Población en general
    ('ALIGN', (0, 2), (0, 2), 'RIGHT'),
    ('FONTNAME', (0, 2), (0, 2), 'OpenSymbol'),
    ('SPAN', (1, 2), (3, 2)),

    # Población de riesgo (niños, ancianos, enfermos, mujeres gestantes, alérgicos/intolerantes)
    ('ALIGN', (0, 3), (0, 3), 'RIGHT'),
    ('FONTNAME', (0, 3), (0, 3), 'OpenSymbol'),
    ('SPAN', (1, 3), (3, 3)),

    # Ambos
    ('ALIGN', (0, 4), (0, 4), 'RIGHT'),
    ('FONTNAME', (0, 4), (0, 4), 'OpenSymbol'),
    ('SPAN', (1, 4), (3, 4)), ])

# Añadimos la tabla al workflow de la página:
story.append(M01_T04)

# Por último, añadimos un separador:
story.append(Spacer(0, 5))

###############################################################################

# Comenzamos definiendo los datos
M01_T05_L00 = ['5. DOCUMENTACIÓN Y REGISTROS:', '', '', '']
M01_T05_L01 = ['\n\n\n\n\n', '', '', '']

# Ahora los unificamos en una sola variable, por comodidad:
M01_T05_DATA = [
    M01_T05_L00, M01_T05_L01, ]

# Definimos las características de la tabla
M01_T05 = Table(M01_T05_DATA, colWidths=((PAGE_WIDTH - (LEFTMARGIN + RIGHTMARGIN)) / 4), splitByRow=1, repeatRows=1)

# Añadimos el estilo general:
M01_T05.setStyle(ESTILO_GENERAL)

# Ahora, añadimos los estilos particulares de cada tabla:
M01_T05.setStyle([

    # 5. DOCUMENTACIÓN Y REGISTROS:
    ('SPAN', (0, 0), (3, 0)),
    ('BACKGROUND', (0, 0), (3, 0), COLOR_FONDO_CABECERA_3),
    ('TEXTCOLOR', (0, 0), (3, 0), COLOR_TEXTO_CABECERA_3),
    ('FONTNAME', (0, 0), (3, 0), 'Helvetica'),
    ('FONTSIZE', (0, 0), (3, 0), 11),

    # Listado de documentos:
    ('SPAN', (0, 1), (3, 1)), ])

# Añadimos la tabla al workflow de la página:
story.append(M01_T05)

# Por último, añadimos un separador:
story.append(Spacer(0, 5))

###############################################################################
# Renderizamos el documento:
# #############################################################################

def myFirstPage(canvas, documento):
    canvas.saveState()
    #canvas.setFont('Times-Bold', 16)
    #canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-108, TITULO)
    #canvas.setFont('Times-Roman', 9)
    #canvas.drawString(cm, 0.75 * cm, "%s" % TEMA)
    canvas.restoreState()

def myLaterPages(canvas, documento):
    canvas.saveState()
    canvas.setFont('Times-Roman', 9)
    canvas.drawString(cm, 0.75 * cm, "%s - Pág. %d" % (TEMA, documento.page))
    canvas.restoreState()

#doc = SimpleDocTemplate(NOMBRE_DOCUMENTO, pagesize=PAPEL, showBoundary=1)
documento = SimpleDocTemplate(
    NOMBRE_DOCUMENTO,
    pagesize = PAPEL,
    # pageTemplates = [],
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

# Construimos el Platypus story.
documento.build(story, onFirstPage=myFirstPage, onLaterPages=myLaterPages)
