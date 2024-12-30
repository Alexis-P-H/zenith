from pypdf import PdfReader

pdf_paths = [
    'coleccionPDFs/sample-1.pdf',
    'coleccionPDFs/Historiasdecronopiosyfamas.pdf'
]


def extractText(colletion):
    try:
        textos = []
        for t in colletion:
            reader = PdfReader(t)
            texto_pdf = ""  # Acumula el texto de todas las páginas de este PDF
            for page in reader.pages:
                texto_pdf += page.extract_text() + "\n"
            textos.append(texto_pdf)  # Añade el texto del PDF actual a la lista
        return textos
    except Exception as e:
        print(f"Se produjo un error: {e}")
        return []


def extractTextFromPageWish(colletion, numeroPagina1, numeroPagina2):
    try:
        textos = []
        for t in colletion:
            reader = PdfReader(t)
            contador = + 1
            if contador == 0:
                numeroPagina = numeroPagina1
            else:
                numeroPagina = numeroPagina2
            for page in reader.pages:
                contador = + 1
                if numeroPagina == contador:
                    texto_pdf = page.extract_text() + "\n"
                    textos.append(texto_pdf)  #Añade el texto del PDF actual a la lista
        return print(textos)
    except Exception as e:
        print(f"Se produjo un error: {e}")
        return []


# extractText(pdf_paths)
extractTextFromPageWish(pdf_paths, 5, 4)


#
# def comparation(collection):
#     try:
#         for i in collection:
#             datecomparated = i
#             a = 0
#             while a < len(collection):
#                 dates_comparated = collection[a]
#                 if datecomparated == dates_comparated:
#                     print(f"se encontró {}")
#                 else:
#                     print("los metadatos no son iguales")
#                 a += 1
#     except exception as e:
#         print(f"error compare metadata from: {e}")
