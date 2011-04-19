#!/usr/bin/env python
# -*- coding: utf-8 -*-

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle as PS
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.platypus import Table

def main():
	f = open ("testTablas.txt", "r")
	story = []
	body = PS (name = 'Body', fontSize = 10, leading = 12)
	P = Paragraph("Ejemplo uso de Tablas",body)
	story.append(P)
	data = [["Posicion","Nombre","Premio"]]
	for l in f.readlines():
		a = l.split(",")
		pos = a[0]
		nom = a[1]
		pre = a[2]
		data.append([pos,nom,pre])

	table = Table(data)
	story.append(table)
	doc = SimpleDocTemplate ("testTable.pdf", pagesize=letter)
	doc.build(story)

if __name__ == "__main__":
    main()
