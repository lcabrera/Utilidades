#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Ejemplos tomados de:
http://www.protocolostomy.com/2008/10/22/generating-reports-with-charts-using-python-reportlab/
'''

import MySQLdb
import sys
import string
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.linecharts import HorizontalLineChart
from reportlab.platypus import *
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch

dbhost = 'localhost'
dbname = 'httplog'
dbuser = 'jonesy'
dbpasswd = 'mypassword'

PAGE_HEIGHT=defaultPageSize[1]
styles = getSampleStyleSheet()
Title = "Generating Reports with Python"
Author = "Brian K. Jones"
URL = "<a class="linkclass" href="http://www.protocolostomy.com">http://www.protocolostomy.com</a>"
email = "<a class="linkclass" href="mailto:bkjones@gmail.com">bkjones@gmail.com</a>"
Abstract = """This is a simple example document that illustrates how to put together a basic PDF with a chart.
I used the PLATYPUS library, which is part of ReportLab, and the charting capabilities built into ReportLab."""
Elements=[]
HeaderStyle = styles["Heading1"]
ParaStyle = styles["Normal"]
PreStyle = styles["Code"]

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

def connect():
   try:
      conn1 = MySQLdb.connect(host = dbhost, user = dbuser, passwd = dbpasswd, db = dbname)
      return conn1
   except MySQLdb.Error, e:
      print "Error %d: %s" % (e.args[0], e.args[1])
      sys.exit (1)

def getcursor(conn):
   cursor = conn.cursor()
   return cursor

def totalevents_hourly(rcursor):
    rcursor.execute("""select hour, count(*) as hits from hits group by hour;""")
    return rcursor

def graphout(catnames, data):
    drawing = Drawing(400, 200)
    lc = HorizontalLineChart()
    lc.x = 30
    lc.y = 50
    lc.height = 125
    lc.width = 350
    lc.data = data
    catNames = catnames
    lc.categoryAxis.categoryNames = catNames
    lc.categoryAxis.labels.boxAnchor = 'n'
    lc.valueAxis.valueMin = 0
    lc.valueAxis.valueMax = 1500
    lc.valueAxis.valueStep = 300
    lc.lines[0].strokeWidth = 2
    lc.lines[0].symbol = makeMarker('FilledCircle') # added to make filled circles.
    lc.lines[1].strokeWidth = 1.5
    drawing.add(lc)
    return drawing

def go():
    doc = SimpleDocTemplate('gfe.pdf')
    doc.build(Elements)

mytitle = header(Title)
myname = header(Author, sep=0.1, style=ParaStyle)
mysite = header(URL, sep=0.1, style=ParaStyle)
mymail = header(email, sep=0.1, style=ParaStyle)
abstract_title = header("ABSTRACT")
myabstract = p(Abstract)
head_info = [mytitle, myname, mysite, mymail, abstract_title, myabstract]
Elements.extend(head_info)

code_title = header("Basic code to produce output")
code_explain = p("""This is a snippet of code. It's an example using the Preformatted flowable object, which
                 makes it easy to put code into your documents. Enjoy!""")
code_source = pre("""
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

hourly_title = header("Hits logged, per hour")
hourly_explain = p("""This shows aggregate hits across a 24-hour period. """)

conn = connect()
cur = getcursor(conn)
te_hourly = totalevents_hourly(cur)
catnames = []
data = []
values = []
for row in te_hourly:
   catnames.append(str(row[0]))
   values.append(row[1])

data.append(values)
hourly_chart = graphout(catnames, data)
hourly_section = [hourly_title, hourly_explain, hourly_chart]
Elements.extend(hourly_section)

go()
