from sqlalchemy import Column, Integer, String, DateTime, create_engine, MetaData, Table
from sqlalchemy.orm import DeclarativeBase

# Crear una instancia del motor de base de datos
engine = create_engine("mysql+mysqldb://root:root@172.21.96.1:3306/db_zenith")

metadata_obj = MetaData()
pdf_metadata = Table(
    'tb_metadata',
    metadata_obj,
    Column("pdf_id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(40), nullable=False),
    Column("autor", String(40), nullable=False),
    Column("producer", String(100), nullable=True),
    Column("title", String(40), nullable=True),
    Column("subject", String(100), nullable=True),
    Column("keywords", String(40), nullable=True),
    Column("creation_date", DateTime, nullable=False),
    Column("mod_date", DateTime, nullable=True),
    Column("creator", String(100), nullable=True),
    Column("document_type", String(100), nullable=True),
    Column("signature", String(100), nullable=True))


# metadata_obj.create_all(engine)
