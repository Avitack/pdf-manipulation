#! python3
# pdf_manipulation.py - Combine PDF in current folder together
import PyPDF2, os

# Get all PDF filenames
pdf_files = []
for fn in os.listdir('.'):
    if fn.endswith('.pdf'):
        pdf_files.append(fn)
pdf_files.sort(key=str.lower)

pdf_writer = PyPDF2.PdfFileWriter()

# Loop through all pdf files
for fn in pdf_files:
    pdf_obj = open(fn, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_obj)
    
    # Loop through all the pages
    for page_num in range(0, pdf_reader.numPages):
        page = pdf_reader.getPage(page_num)
        pdf_writer.addPage(page)

# Save the merged pdf to file
pdf_output = open('merged.pdf', 'wb')
pdf_writer.write(pdf_output)
pdf_output.close()
