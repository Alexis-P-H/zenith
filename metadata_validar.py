import os
from pypdf import PdfReader


def extract_metadata(pdf_paths):
    """
    Extrae los metadatos de una lista de archivos PDF y los compara.
    """
    metadata_collection = []
    try:
        for path in pdf_paths:
            if os.path.exists(path):  # Verifica que el archivo exista
                reader = PdfReader(path)
                metadata = reader.metadata  # Obtiene los metadatos del archivo
                metadata_collection.append(metadata)
                print(f"Metadatos extraídos de {path}: {metadata}")
            else:
                print(f"Archivo no encontrado: {path}")
    except Exception as e:
        print(f"Error al extraer metadatos de {path}: {e}")

    return compare_metadata(metadata_collection)


def compare_metadata(metadata_collection):
    """
    Compara los metadatos entre todos los archivos proporcionados.
    """
    if len(metadata_collection) < 2:
        print("No hay suficientes archivos para comparar.")
        return False
    try:
        for i in range(len(metadata_collection)):
            for j in range(i + 1, len(metadata_collection)):
                if metadata_collection[i] == metadata_collection[j]:
                    print(f"Metadatos iguales entre los archivos {i + 1} y {j + 1}.")
                else:
                    print(f"Metadatos diferentes entre los archivos {i + 1} y {j + 1}.")
                    dato1 = metadata_collection[i]
                    dato2 = metadata_collection[j]
                    print(f"dato1: {dato1} \n"
                          f"dato2: {dato2}")
    except Exception as e:
        print(f"Error al comparar metadatos: {e}")
        return False
    return True


