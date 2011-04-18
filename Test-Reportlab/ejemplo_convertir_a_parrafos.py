#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Módulos necesarios para la generación del archivo

from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
import os
import sys


class GenerarPDF:

    def __init__(self, arcini, arcfin):
        self.arcini = arcini
        self.arcfin = arcfin

    def crear(self):

        # Creamos un objeto getSampleStyleSheet para usar

        estilo = getSampleStyleSheet()

        # Se instancia SimpleDocTemplate para estructurar el archivo

        pdf = SimpleDocTemplate(self.arcfin, pagesize=letter)

        # Esta lista contendra la info para guardar

        historia = []

        # Cargamos un archivo de texto para volverlo pdf

        texto = file(self.arcini).read()

        # Separamos cada nueva linea en una lista

        paragrafo = texto.split('\n')

        # Leemos cada indice de la lista

        for h in paragrafo:

            # Vamos agregando los datos a la lista, con un 0.1 de pulgada
            # de distancia

            historia.append(Paragraph(h, estilo['Normal']))
            historia.append(Spacer(0, inch * .1))

        # Generamos el pdf

        pdf.build(historia)

        print 'El archivo %s fue generado satisfactoriamente' \
            % self.arcfin


# Si en la ejecución no pasamos 3 parámetros

if len(sys.argv) < 3:
    print 'Uso: python <script> archivo_de_entrada archivo.pdf'
    sys.exit()
else:
    obj = GenerarPDF(sys.argv[1], sys.argv[2])
    obj.crear()

