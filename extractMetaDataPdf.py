import os
from pypdf import PdfReader

pdf_path = os.path.join('processPDFs', 'meta-pdf.pdf')
pdf_modified_path = os.path.join('processPDFs', 'meta-pdf.pdf')

def extract_metadata(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        meta = reader.metadata
        return meta
    except Exception as e:
        print(f"Error extracting metadata: {e}")
        return None

def compare_metadata(original_date, modified_date):
    if modified_date != original_date:
        print("El PDF fue modificado, por favor revisar que sea el PDF correcto")
    else:
        print("Ese PDF está más melo que un melo, ¡¡PDF procesado!!")

original_pdf_date = extract_metadata(pdf_path)
modified_pdf_date = extract_metadata(pdf_modified_path)

print(original_pdf_date , "\n\n", modified_pdf_date)

compare_metadata(original_pdf_date, modified_pdf_date)
