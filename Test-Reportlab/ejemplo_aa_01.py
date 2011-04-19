#!/usr/bin/env python
# -*- coding: utf-8 -*-

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter,A4,A5,A3

c = canvas.Canvas("ej0.pdf",pagesize=letter)
c.drawString(50,500, "MI PRIMER PDF")
c.drawString(250,300,"Cordenada = (250,300) ")
c.drawString(150,400,"APRENDIENDO REPORTLAB")
c.showPage()
c.save()