#!/usr/bin/env python
# -*- coding: utf-8 -*-

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle as PS
from reportlab.platypus import SimpleDocTemplate, PageBreak, Paragraph

story = []

h1 = PS (name = 'Heading 1', fontSize = 14, leading = 16)
h2 = PS (name = 'Heading 2', fontSize = 12, leading = 14)
body = PS (name = 'Body', fontSize = 10, leading = 12)
P = Paragraph("Estilo Cabecera h1", h1)
story.append(P)
P = Paragraph("Estilo h2", h2)
story.append(P)
story.append(PageBreak())
P = Paragraph("Prueba de BodyText", body)
story.append(P)

doc = SimpleDocTemplate ("ej1.pdf", pagesize=letter, showBoundary=0)
doc.build(story)