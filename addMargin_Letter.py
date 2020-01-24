import PyPDF2
from PyPDF2 import PdfFileReader, PdfFileWriter

# Create a pdf object
pdfFileObj = open('lecture1.pdf', 'rb')
# pdfFileObj = open('w1_KNN.pdf', 'rb')
# read the pdf object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# create pdf writer object
writerObj = PdfFileWriter()

def isVertical(page):
    page = page.mediaBox
    return page.getUpperRight_x() - page.getUpperLeft_x() < page.getUpperRight_y() - page.getLowerRight_y()

for i in range(pdfReader.getNumPages()):
    # page = pdfReader.getPage(1)
    page = pdfReader.getPage(i)
    
    width = float(page.mediaBox.getWidth())
    height = float(page.mediaBox.getHeight())
    # if height > width:
        # width = height
    # else:
        # height = width
    
    # make the width smaller than 612
    
    if page.get('/Rotate') and page.get('/Rotate') % 180 != 0: 
        rotate = 1
        width *= 400 / height
        height = 400
        
        page.scaleTo(width, height)
        
        delta = height - 612
        
        page.mediaBox.setLowerLeft((0, delta))
        page.mediaBox.setLowerRight((width, delta))
        page.mediaBox.setUpperLeft((0, height))
        page.mediaBox.setUpperRight((width, height))
        page.cropBox.setLowerLeft((0, delta))
        page.cropBox.setLowerRight((width, delta))
        page.cropBox.setUpperLeft((0, height))
        page.cropBox.setUpperRight((width, height))

    else:
        rotate = 0 
        
        page.scale(400 / width, 400 / width)
    
        width = 612
        
        page.mediaBox.setLowerLeft((0, 0))
        page.mediaBox.setLowerRight((width, 0))
        page.mediaBox.setUpperLeft((0, height))
        page.mediaBox.setUpperRight((width, height))
        page.cropBox.setLowerLeft((0, 0))
        page.cropBox.setLowerRight((width, 0))
        page.cropBox.setUpperLeft((0, height))
        page.cropBox.setUpperRight((width, height))
    
    # Write the new page
    writerObj.addPage(page)

# Create an output pdf
with open('temp.pdf', 'wb') as outstream:
    writerObj.write(outstream)
    