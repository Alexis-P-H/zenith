import os
from datetime import datetime
from pypdf import PdfReader, PdfWriter

pdf = os.path.join('coleccionPDFs/', 'sample-1.pdf')
reader = PdfReader(pdf)
writer = PdfWriter()

for page in reader.pages:
    writer.add_page(page)

    if reader.metadata is not None:
        writer.add_metadata(reader.metadata)

    utc_time = "-05'00'"
    time = datetime.now().strftime(f"D\072%Y%m%d%H%M%S{utc_time}")

    writer.add_metadata(
        {
            "/Author": "DIAN",
            "/Producer": "Editorial PDFeos",
            "/Title": f"Documento No.1",
            "/Subject": "Documento equivalente",
            "/Keywords": "Factura",
            "/CreationDate": time,
            "/ModDate": time,
            "/Creator": "Editorial PDFeos Cadena S.A",
            "/CustomField": "Este pdf está aprobado por la DIAN no me vengan con cuentos canticos de ballena",
        }
    )

    with open(f"processPDFs/meta-pdf.pdf", "wb") as f:
        writer.write(f)




# ***** MASIVO ******
# i = 1
#
# folder = 'coleccionPDFs'
# folderLen = len([f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))])
#
# print(folderLen)
#
# print(type(folderLen))
#
# while i <= folderLen:
#     pdfRoot = os.path.join('rpdfs/', f'sample-{i}.pdf')
#     reader = PdfReader(pdfRoot)
#     writer = PdfWriter()
#
#     for page in  reader.pages:
#         writer.add_page(page)
#
#     if reader.metadata is not None:
#         writer.add_metadata(reader.metadata)
#
#     utc_time = "-05'00'"
#     time = datetime.now().strftime(f"D\072%Y%m%d%H%M%S{utc_time}")
#
#     writer.add_metadata(
#         {
#             "/Author": "DIAN",
#             "/Producer": "Editorial PDFeos",
#             "/Title": f"Documento No.{i}",
#             "/Subject": "Documento equivalente",
#             "/Keywords": "Factura",
#             "/CreationDate": time,
#             "/ModDate": time,
#             "/Creator": "Editorial PDFeos Cadena S.A",
#             "/CustomField": "Este pdf está aprobado por la DIAN no me vengan con cuentos canticos de ballena",
#         }
#     )
#
#     with open(f"processPDFs/meta-pdf-{i}.pdf", "wb") as f:
#         writer.write(f)
#
#     i += 1

