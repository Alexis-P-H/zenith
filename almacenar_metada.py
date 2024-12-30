from datetime import datetime
from sqlalchemy.orm import Session
from pypdf import PdfReader
import os
from metadata_model import engine, pdf_metadata


def almacenar_metadatafn(pdf_paths):
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

                with Session(engine) as session:
                    for pdf in metadata_collection:
                        cleaned_date_created = pdf['/CreationDate'][2:16]
                        cleaned_date_mod = pdf['/ModDate'][2:16]
                        formatted_date_created = datetime.strptime(cleaned_date_created, "%Y%m%d%H%M%S").strftime("%Y-%m-%d %H:%M:%S")
                        formatted_date_mod = datetime.strptime(cleaned_date_mod, "%Y%m%d%H%M%S").strftime("%Y-%m-%d %H:%M:%S")

                        insert_data_pdf = pdf_metadata.insert().values(
                            name=path,
                            autor=pdf['/Author'],
                            producer=pdf['/Producer'],
                            title=pdf['/Title'],
                            subject=pdf['/Subject'],
                            keywords=pdf['/Keywords'],
                            creation_date=formatted_date_created,
                            mod_date=formatted_date_mod,
                            creator=pdf['/Creator'],
                            document_type='Documento Equivalente',
                            signature='/Firma'
                        )
                        result = session.execute(insert_data_pdf)
                        session.commit()
                        print(result.rowcount)
            else:
                print(f"Archivo no encontrado: {path}")
        print("Datos insertados con exito")
    except Exception as e:
        print("error:", e)


