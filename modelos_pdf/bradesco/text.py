import pdfplumber

def Total_Paginas(file):
    with pdfplumber.open(file) as pdf:
        total = len(pdf.pages)
        return total