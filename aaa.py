# import packages
import PyPDF2
import re

# open the pdf file
object = PyPDF2.PdfFileReader("E:/Gurov_SSD_256/My_docs/CV/CV_to_Vit_Krasnik_updated_with_Native_Digital.pdf")

# get number of pages
NumPages = object.getNumPages()
print(NumPages)

# define keyterms
String = "Gurov"

# extract text and do the search
for i in range(0, NumPages):
    PageObj = object.getPage(i)
    print("this is page " + str(i + 1))
    Text = PageObj.extractText()
    # print(Text)
    ResSearch = re.search(String, Text)
    print(ResSearch)