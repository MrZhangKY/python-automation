import PyPDF2, os

#get all pdf files from basePath and sort these files by their names
basePath = r''
pdfList = []
for file in os.listdir(basePath):
    if file.endswith('.pdf'):
        pdfList.append(file)
pdfList.sort()

#create PdfFileWriter to store and merge pdf files
pdfWriter = PyPDF2.PdfFileWriter()

#open the pdf files and store each page in PdfFileWriter
for pdf in pdfList:
    pdfReader = PyPDF2.PdfFileReader(open(os.path.join(basePath, pdf), 'rb'))
    print(pdfReader.numPages)
    for pageNum in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
        
#save the PdfFileWriter to a file
pdfWriter.write(open('pdfMergeResult.pdf', 'wb'))