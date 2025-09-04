# Importamos lo necesario para definir tablas y columnas en SQLAlchemy
from sqlalchemy import Column, Integer, String

# Importamos la clase Base que declaramos en database.py
# Aquí es donde se registran las tablas de SQLAlchemy
from database import Base

# -------------------------------------------
# Modelo Order
# Representa la tabla "orders" en la base de datos.
# Cada atributo de la clase corresponde a una columna.
# -------------------------------------------
class Order(Base):
    __tablename__ = "orders"  # Nombre de la tabla en la DB

    # Definimos las columnas de la tabla:
    id = Column(Integer, primary_key=True, index=True)  # Clave primaria
    cliente = Column(String, index=True)                # Nombre del cliente
    dron = Column(String)                               # Modelo del dron
    descripcion = Column(String)                        # Descripción del problema
    estado = Column(String)                             # Estado de la orden
    fecha_ingreso = Column(String)                      # Fecha de ingreso
    fecha_entrega = Column(String, nullable=True)       # Fecha de entrega (puede estar vacía)
