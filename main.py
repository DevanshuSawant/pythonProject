# importing required modules

import PyPDF2

# creating a pdf file object
pdfFileObj = open('aids-sem2.pdf', 'rb')
# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# printing number of pages in pdf file
print(pdfReader.numPages)
# creating a page object
pageObj = pdfReader.getPage(1)
# extracting text from page
print(pageObj.extractText())

# save the extracted data from pdf to a txt file
# we will use file handling here
# dont forget to put r before you put the file path
# go to the file location copy the path by right clicking on the file
# click properties and copy the location path and paste it here.
# put "\\your_txtfilename"
file1 = open(r"1.txt", "wb")
file1.writelines(pageObj.extractText())
# closing the pdf file object
pdfFileObj.close()
