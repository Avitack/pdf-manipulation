#! python3
# pdf_manipulation.py - Combine PDF in current folder together
import PyPDF2, os


def print_menu():
    print("####################\n  pdf-manipulation\n####################\n")
    print("Note: Currently all options work on all the pdf files in the same folder as this script")
    print("Menu:")
    print("\n1. - Create/Merge (1)")
    print("\n2. - Add Watermark (2)")
    print("\n3. - Delete page(s) (not implemented)")
    print("\n4. - Rotate pages(s) (not implemented)")

def entry_point():
    print_menu()
    option = input("\nChoose an option: ")
    if option == "1":
        merge()
    elif option == "2":
        add_watermark()
    else:
        print_menu()

def merge():
    
    output_name = input("Enter name of merged .pdf file (default: 'merged.pdf'): ")
    if output_name == '':
        output_name = 'merged.pdf'
    if output_name[-4:] != '.pdf':
        output_name = output_name + '.pdf'
    
    pdf_files = get_all_pdf_filenames()
    pdf_writer = PyPDF2.PdfFileWriter()

    # loop through all pdf files
    for fn in pdf_files:
        pdf_obj = open(fn, 'rb')
        pdf_reader = PyPDF2.PdfFileReader(pdf_obj)
        
        # loop through all the pages
        for page_num in range(0, pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            pdf_writer.addPage(page)

    # save the merged pdf to file
    pdf_output = open(output_name, 'wb')
    pdf_writer.write(pdf_output)
    pdf_output.close()
    print("Created merged file: " + output_name)

def add_watermark():
    watermark = input("Enter name of watermark .pdf file: ")
    if watermark == '':
        return
    if watermark[-4:] != '.pdf':
        watermark = watermark + '.pdf'

    pdf_files = get_all_pdf_filenames(watermark)

    pdf_watermark_reader = PyPDF2.PdfFileReader(open(watermark, 'rb'))

    # loop through all pdf files
    for fn in pdf_files:
        pdf_obj = open(fn, 'rb')
        pdf_reader = PyPDF2.PdfFileReader(pdf_obj)
        first_page = pdf_reader.getPage(0)
        first_page.mergePage(pdf_watermark_reader.getPage(0))
        pdf_writer = PyPDF2.PdfFileWriter()
        pdf_writer.addPage(first_page)
        
        # loop through all the pages
        for page_num in range(1, pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            pdf_writer.addPage(page)
        
        # save the watermarked pdf files to file
        output_name = fn[:-4] + '_Watermarked.pdf'
        pdf_output = open(output_name, 'wb')
        pdf_writer.write(pdf_output)
        pdf_obj.close()
        pdf_output.close()
        print("Created watermarked file: " + output_name)
    
def get_name_from_user(prompt, default):
    return

def get_all_pdf_filenames(exclude=''):
    
    # get all PDF filenames
    pdf_files = []
    for fn in os.listdir('.'):
        if fn.endswith('.pdf'):
            if fn != exclude:
                pdf_files.append(fn)
    pdf_files.sort(key=str.lower)
    return pdf_files

entry_point()
