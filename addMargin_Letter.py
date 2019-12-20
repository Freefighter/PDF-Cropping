import PyPDF2
from PyPDF2 import PdfFileReader, PdfFileWriter

# Create a pdf object
pdfFileObj = open('w1_KNN.pdf', 'rb')
# read the pdf object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# create pdf writer object
writerObj = PdfFileWriter()


for i in range(pdfReader.getNumPages()):
    # page = pdfReader.getPage(1)
    page = pdfReader.getPage(i)
    
    width = page.mediaBox.getWidth()
    height = page.mediaBox.getHeight()
    # if height > width:
        # width = height
    # else:
        # height = width
    if width < 612:
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
    