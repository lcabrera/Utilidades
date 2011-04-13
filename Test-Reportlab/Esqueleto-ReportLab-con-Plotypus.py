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

# Obtenemos de  platypus las  clases Paragraph, para  escribir párrafos
# Image,  para insertar  imágenes y  SimpleDocTemplate para  definir el
# DocTemplate. Además importamos Spacer, para incluir espacios .

from reportlab.platypus import Paragraph
from reportlab.platypus import Image
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Spacer

# Si queremos tablas...
from reportlab.platypus import Table

# Importamos clase de hoja de estilo de ejemplo.

from reportlab.lib.styles import getSampleStyleSheet

# Se importa el tamaño de la hoja.

from reportlab.lib.pagesizes import A3
from reportlab.lib.pagesizes import A4

# Y los colores.

from reportlab.lib import colors

IMAGEN = '/home/lcabrera/Imágenes/CAFETERIA/Printer.Ticket.Logo.NUEVO_192x92.png'

# Creamos un PageTemplate de ejemplo.

estiloHoja = getSampleStyleSheet()

# Inicializamos la lista Platypus Story.

story = []

# Definimos cómo queremos que sea el estilo de la PageTemplate.

cabecera = estiloHoja['Heading4']

#  No se  hará un  salto de  página después  de escribir  la cabecera
# (valor 1 en caso contrario).

cabecera.pageBreakBefore = 0

# Se  quiere que  se empiece  en la  primera página  a escribir.  Si es
# distinto de 0 deja la primera hoja en blanco.

cabecera.keepWithNext = 0

# Color de la cabecera.

cabecera.backColor = colors.cyan

# Incluimos un Flowable, que en este caso es un párrafo.

parrafo = Paragraph('CABECERA DEL DOCUMENTO ', cabecera)

# Lo incluimos en el Platypus story.

story.append(parrafo)

# Definimos  un párrafo. Vamos  a crear  un texto largo  para demostrar
# cómo se genera más de una hoja.

cadena = ' El Viaje del Navegante ' * 600

# Damos un estilo BodyText al segundo párrafo, que será el texto a escribir.

estilo = estiloHoja['BodyText']
parrafo2 = Paragraph(cadena, estilo)

# Y lo incluimos en el story.

story.append(parrafo2)

# Dejamos espacio.

story.append(Spacer(0, 20))

# Ahora incluimos una imagen.

fichero_imagen = IMAGEN
imagen_logo = Image(os.path.realpath(fichero_imagen), width=192, height=192)
story.append(imagen_logo)

# Dejamos algo de espacio:
story.append(Spacer(0, 20))

# Definimos las filas de una tabla.

fila1 = ['','Lunes','Martes','Miércoles','Jueves','Viernes','Sábado','Domingo']
fila2 = ['Mañana','Estudiar','Gimnasio','-','-','-','Estudiar','Ir a la iglesia']
fila3 = ['Tarde','Trabajar','Trabajar','Trabajar','Trabajar','Trabajar','-','-']
fila4 = ['Noche','Trabajar','Trabajar','Trabajar','Trabajar','-','-','-']

# Definimos la tabla.

tabla = Table([fila1,fila2,fila3,fila4])

# Podemos dar estilo a los elementos de una tabla. En esta ocasión vamos
# a poner de color azul Mañana,Tarde y Noche y en color rojo los días de
# la semana.

tabla.setStyle([
    ('TEXTCOLOR',(1,-4),(7,-4),colors.red),
    ('TEXTCOLOR',(0,0),(0,3),colors.blue)
    ])

# Y la asignamos al platypus story.

story.append(tabla)

# Darse cuenta de las coordenadas en SetStyle a la hora de cambiar el
# color. El resultado, si se incluye este código en el ejemplo anterior,
# justo después de la imagen, es el siguiente:
# http://1.bp.blogspot.com/_y_bGxMwbE9g/S7i8rcR101I/AAAAAAAAAZg/kA7J877xv4M/s400/aplicpdf5.JPG

# Sucesivos usos del método setStyle aplica estilos de forma aditiva. Así
# por ejemplo tendremos que:

# Damos color de fondo a las celdas.

tabla.setStyle([('BACKGROUND',(1,1),(-1,-1),colors.cyan)])

# Creamos una caja alrededor de las celdas.

tabla.setStyle([('BOX',(1,1),(-1,-1),0.25,colors.black)])

# Y ponemos una malla (rejilla) a la tabla.

tabla.setStyle([('INNERGRID',(1,1),(-1,-1),0.25,colors.black)])

# Dando como resultado:
# http://2.bp.blogspot.com/_y_bGxMwbE9g/S7i9EPBz6KI/AAAAAAAAAZo/hrW694lcCO8/s400/aplicpdf6.JPG

# Se pueden  hacer muchísimas cosas más con tablas.  Animo al lector a
# investigar más sobre el tema en el manual de ReportLab.

# Para terminar solo comentar que si se quiere incluir un nuevo elemento
# en el documento  solo es necesario ir añadiendo a  la lista de platypus
# story los flowables que se quieran.

#######################################################################
##
## SEGUIR EN:
##
## http://elviajedelnavegante.blogspot.com/2010/04/crear-documentos-pdf-en-python-y-3.html
##
#######################################################################


# Creamos un  DocTemplate en  una hoja DIN  A4, en la  que se  muestra el
# texto enmarcado (showBoundary=1) por un recuadro.

doc = SimpleDocTemplate(
        'Ejemplo-Reportlab-con-Plotypus.pdf',
        pagesize=A3,
        showBoundary=1)

# Construimos el Platypus story.

doc.build(story)

