import PyPDF2
from PyPDF2 import PdfFileReader, PdfFileWriter
import sys, os


def addMargin(doc):
    # Create a pdf object
    pdfFileObj = open(doc, 'rb')
    # read the pdf object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    # create pdf writer object
    writerObj = PdfFileWriter()


    for i in range(pdfReader.getNumPages()):
        # page = pdfReader.getPage(1)
        page = pdfReader.getPage(i)
        
        width = page.mediaBox.getWidth()
        height = page.mediaBox.getHeight()
        if height > width:
            # delta = height - width
            # width = height
            
            delta = 204
            
            page.mediaBox.setLowerLeft((-delta, 0))
            page.mediaBox.setLowerRight((width+delta, 0))
            page.mediaBox.setUpperLeft((-delta, height))
            page.mediaBox.setUpperRight((width+delta, height))
            page.cropBox.setLowerLeft((-delta, 0))
            page.cropBox.setLowerRight((width+delta, 0))
            page.cropBox.setUpperLeft((-delta, height))
            page.cropBox.setUpperRight((width+delta, height))
            
        
        # Write the new page
        writerObj.addPage(page)
        print("page %d done"%i)
            
    # Create an output pdf
    # with open('\%USERPROFILE\%\\Desktop\\temp_%s' + os.path.basename(doc), 'wb') as outstream:
    with open('{}\\Desktop\\temp_{}'.format(os.environ['USERPROFILE'], 
        os.path.basename(doc)), 'wb') as outstream:
        writerObj.write(outstream)
    print("write")
    
    # 最后再关，否则之前输出变空白
    pdfFileObj.close()
    
if __name__ == "__main__":
    # sys.argv[0:] 指此py文件的名称
    docs = [os.path.normpath(path) for path in sorted(sys.argv[1:])]
    for doc in docs:
        addMargin(doc)