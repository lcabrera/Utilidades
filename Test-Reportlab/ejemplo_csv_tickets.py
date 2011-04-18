#! /usr/bin/env python
#coding=utf-8

DEBUG = True

# Miscellaneous
from cStringIO import StringIO
import random
import re

# Process CSV files
import csv

# Generate PDFs using ReportLab
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import *
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import LETTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch, mm
from reportlab.graphics.barcode import code39

PAGE_HEIGHT= 11 * inch
PAGE_WIDTH= 8.5 * inch
styles = getSampleStyleSheet()
Title = "ELS Graduation Regalia Checklist"

def process_csv(fn):
    ''' Process a csv file containing lastname and firstname.
    Return a list of lists containing lastname, firstname, and random identifier
    '''
    data =  []
    choices = range(100000)
    csvfile = csv.reader(open(fn))
    # throw away header
    csvfile.next()
    for row in csvfile:
        if DEBUG: print row
        newdata = [row[0],row[1],row[0][:3].upper() +'-'+str(random.choice(choices))]
        if DEBUG: print newdata
        data.append(newdata)
    return data

def docPage(canvas, doc):
    canvas.saveState()
    canvas.setFont('Times-Bold', 10)
    canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT - (.25 * inch), Title)
    canvas.setFont('Times-Roman',9)
    canvas.drawString(7 * inch, .75 * inch, "Page %d" % (doc.page,))
    canvas.restoreState()

def ticketPage(canvas, doc ):
    canvas.saveState()
    H = 1.5 * inch
    W = 1.5 * .69 * inch
    canvas.drawImage('boliche.png', 6 * inch, PAGE_HEIGHT - (1.75 * inch), width = W, height = H)
    canvas.restoreState()

def gen_key(data, fn):
    doc = SimpleDocTemplate(fn)
    Story = []
    tabledata = []
    style = styles["Normal"]
    tabledata.append(['Graduating student','Regalia code','Picked up?'])
    for row in data:
        tabledata.append(["%s, %s" % (row[0], row[1]), "%s" % row[2],"[                ]"])
    t=Table(tabledata, colWidths= 2 * inch, repeatRows=1)
    Story.append(t)
    doc.build(Story, onFirstPage=docPage, onLaterPages=docPage)

def gen_ticket(row,fn):
    "Generate a regalia ticket as a separate PDF document."
    doc = SimpleDocTemplate(fn)
    Story = []
    styleN = styles["Normal"]
    styleH = styles['Heading1']
    Story.append(Paragraph("ELS Graduation 2010 Regalia Ticket",styleH))
    Story.append(Spacer(1 * inch, .5 * inch))
    Story.append(Paragraph("Student name: %s, %s" % (row[0], row[1]), styleN))
    Story.append(Spacer(1 * inch, .25 * inch))
    Story.append(Paragraph("Student regalia code: <strong>%s</strong>" % (row[2]), styleN))
    Story.append(Spacer(1 * inch, .5 * inch))
    barcode=code39.Extended39(row[2], barWidth= 0.02 * inch, barHeight= .5 * inch)
    Story.append(barcode)
    doc.build(Story, onFirstPage=ticketPage, onLaterPages=ticketPage)
    return

# create an re to get rid of non-word chars for file names
pattern = re.compile('[\W_]+')

data = process_csv('ejemplo_csv_tickets.csv')
for row in data:
    fname =  pattern.sub('-', row[0] + '-'+ row[1]).lower()
    fname += ".pdf"
    gen_ticket(row, fname)
gen_key(data, "zzzzzzzz.pdf")