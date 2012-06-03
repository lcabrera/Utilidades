#! /usr/bin/env python
"""
This module assumes that you are comparing only two data sets, and that
both of them are lists (or tuples or any naturally iterable object)
of the same length.

Note: 1 inch = 72 points
"""
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib import colors # dir(colors) after this import to see the variety of options
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from reportlab.graphics.shapes import * 

######################################################
# STANDALONE DATA EXAMPLES
# These are just here if you want to run the example as an executable from the command-line.
# The reverse() only exists for fun... if you can call Python nerdery "fun".
# Import and pass your own two data lists as args to generate() for your own results.

DATA1 = range(31,69) # DATA1.__len__() & len(DATA1) is 38
DATA2 = range(19,57) # DATA2.__len__() & len(DATA2) is also 38
DATA2.reverse()

######################################################
# VARIABLES

MARGIN  = 0.75 * inch
DATA1_COLOR = '#9B5858' # Use colors.[whatever] if you prefer non-hex
DATA2_COLOR = '#9D9D9D'
GRID_COLOR  = '#DDDDDD'
OUTPUT_NAME = 'sample.pdf'

######################################################
# CONSTANTS -- DO NOT EDIT

NUMBER_OF_DATA_SETS = 2
PAGE_HEIGHT = letter[0] # 612 = 8.5in.
PAGE_WIDTH = letter[1] # 792 = 11in.
# This PAGE_PADDING seems to be the required gutter (for both sides)
# for rendering w/o errors when the MARGIN above is set to zero.
PAGE_PADDING = 0.167 * inch
MAX_GRAPH_HEIGHT = PAGE_HEIGHT - 2 * MARGIN - PAGE_PADDING 
MAX_GRAPH_WIDTH = PAGE_WIDTH - 2 * MARGIN - PAGE_PADDING

def myFirstPage (canvas, doc):
    canvas.saveState()
    canvas.restoreState()

def myLaterPages (canvas, doc):
    canvas.saveState()
    canvas.restoreState()

def generate(DATA1, DATA2):
    # Set the origin of the graph.
    # X_POSITION will increase as the chart data is analyzed and plotted
    # left-to-right. It must be reset to MARGIN before proceeding with page 2.
    X_POSITION, Y_POSITION = MARGIN, MARGIN

    # Figure out the column width.
    # How much space do you want between each set of bars?
    SPACE_FACTOR = 0.5 # Half the size of one data bar.

    # Divide the maximum printable area by the total number of bars & spaces, based on your data set.
    # This gives us the individual column width in points.
    COL_W = MAX_GRAPH_WIDTH / ( len(DATA1) * ( NUMBER_OF_DATA_SETS + SPACE_FACTOR ) )

    # Now get the width of the spacer in points.
    SP_W = COL_W * SPACE_FACTOR
    SPACER = Rect(X_POSITION, Y_POSITION, SP_W, 0, fillColor=colors.white, strokeColor=None)

    # Determine how to squish down any possible sets of data so they all fit on
    # one page (and the MAX_GRAPH parameters), regardless of the data itself.
    MAX_OF_ALL = max(max(DATA1), max(DATA2)) # highest value of both data sets
    MIN_OF_ALL = min(min(DATA1), min(DATA2)) # lowest value of both data sets
    # Find the highest value where we will draw a grid line;
    # none of the data points will exceed this value.
    MAX_CHART = range(0, int(round(MAX_OF_ALL)) + 10, 10)[-1]
    # Find the lowest value where we will draw a grid line;
    # no data point will be lower than this, and it will be the origin on the y-axis.
    MIN_CHART = range(0, int(round(MIN_OF_ALL)), 10)[-1]
    
    # Figure out the multiplier. This number represents how tall (in points) that
    # a data bar on the graph would be if its value was 1.
    MULTIPLIER = MAX_GRAPH_HEIGHT / (MAX_CHART - MIN_CHART)

    # Now we're ready to proceed
    # Note that zip() will handle as many different lists as required, OTB.
    DATA_LIST = zip(DATA1, DATA2) # list of tuples

    # Instantiate the necessary element classes.
    doc = SimpleDocTemplate(OUTPUT_NAME,
                            pagesize=(PAGE_WIDTH, PAGE_HEIGHT), # Landscape orientation
                            leftMargin = 0,
                            rightMargin = 0,
                            bottomMargin = 0,
                            topMargin = 0,
                            )
    Story = []
    d = Drawing( PAGE_WIDTH, ( PAGE_HEIGHT - PAGE_PADDING ) )

    # Process the data sets.
    for tuple in DATA_LIST:
        n1, n2 = tuple[0], tuple[1]
        # Info from DATA1
        d.add( Rect( X_POSITION, Y_POSITION, COL_W, (n1 - MIN_CHART) * MULTIPLIER, fillColor=DATA1_COLOR, strokeColor=None ) )
        X_POSITION += COL_W # move X_POSITION to the right 1 column width
        # Info from DATA2
        d.add( Rect( X_POSITION, Y_POSITION, COL_W, (n2 - MIN_CHART) * MULTIPLIER, fillColor=DATA2_COLOR, strokeColor=None))
        X_POSITION += COL_W # move X_POSITION to the right 1 column width
        d.add(SPACER)
        X_POSITION += SP_W # move X_POSITION to the right 1 spacer width

    # Draw data-independent objects.
    for x in range( MIN_CHART, MAX_CHART + 1, 10):
        # y-axis labels
        d.add( String( MARGIN/2, Y_POSITION + ((x - MIN_CHART - 0.5) * MULTIPLIER), str(x), fontSize=12, fillColor=colors.black))
        # Horizontal grid lines
        d.add( Line( MARGIN, Y_POSITION + ((x - MIN_CHART) * MULTIPLIER), X_POSITION, Y_POSITION + ((x - MIN_CHART) * MULTIPLIER), strokeColor=GRID_COLOR, strokeWidth=1))

    # Drop the Drawing onto the page.
    Story.append(d)

    # Construct the PDF.
    doc.build(Story, onFirstPage=myFirstPage, onLaterPages=myLaterPages)

# ------------------------------------------

if __name__ == '__main__':
    generate(DATA1, DATA2)

######################################################
# Object Reference Only
# d = Drawing(width??, distance below previous drawing or object or page edge)
# Rect ( x from left of Drawing origin,
        # y from bottom of Drawing origin,
        # width of bar,
        # height of bar,
        # fillColor,
        # strokeColor)
# Line (startx, starty, endx, endy, strokeColor, strokeWidth)
