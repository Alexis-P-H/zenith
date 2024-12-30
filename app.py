from text_validWords import extractText
from metadata_validar import extract_metadata
from almacenar_metada import almacenar_metadatafn


# Lista de rutas de los archivos PDF
pdf_paths = [
    'processPDFs/meta-pdf-modify.pdf',
    'processPDFs/meta-pdf.pdf'
]


def mostrar_menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Opción 1: Extraer y validar la metadata de los PDFS")
    print("2. Opción 2: Extraer texto de pdfs")
    print("3. Opción 3: Almacenar metadata")
    print("3. Opción 4: en proceso: Comparar textos de PDFS")
    print("4. Opción 5: salir")

def main():
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Selecciona una opción: "))
            if opcion == 1:
                # Recolecta y compara metadatos
                extract_metadata(pdf_paths)
            elif opcion == 2:
                # Devuelve el texto de cada pdf en la colección
                extractText(pdf_paths)
            elif opcion == 3:
                almacenar_metadatafn(pdf_paths)
            elif opcion == 4:
                print("Saliendo del programa. ¡Hasta luego!")
                break
            else:
                print("Por favor, selecciona una opción válida (1-4).")
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número.")


if __name__ == "__main__":
    main()
