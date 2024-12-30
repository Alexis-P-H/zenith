import os
from datetime import datetime
from pypdf import PdfReader, PdfWriter


def writeMetada(pdf_paths):
    try:
        for path in pdf_paths:
            if os.path.exists(path):  # Verifica que el archivo exista
                reader = PdfReader(path)
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
                            "/DocumentType": "FV, NC, ND, NM, POS, Documento Equivalente, Contrato",
                            "/Firma": "Generación de PDF - Cadena S.A"
                        }
                    )
                path = path.replace("processPDFs/", "")
                with open(f"processPDFs/{path}", "wb") as f:
                    writer.write(f)

                print("Se escribe la metadata para el pdf", path)
            else:
                print(f"Archivo no encontrado: {path}")
    except Exception as e:
        print(f"Error al extraer metadatos de {path}: {e}")








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

