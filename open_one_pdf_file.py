# importing required modules
import PyPDF2

# creating a pdf file object
pdfFileObj = open('E:/Gurov_SSD_256/My_docs/CV/CV_to_Vit_Krasnik_updated_with_Native_Digital.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# printing number of pages in pdf file
print(pdfReader.numPages)

# creating a page object
pageObj = pdfReader.getPage(0)

# extracting text from page
actual_text = pageObj.extractText()
expected_text = "Gur"
assert expected_text in pageObj.extractText()
print(f'Expected "{expected_text}", and got: "{actual_text}" ')

# closing the pdf file object
pdfFileObj.close()
