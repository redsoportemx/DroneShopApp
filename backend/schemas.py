# Importamos BaseModel de Pydantic, que se usa para validar datos
from pydantic import BaseModel
from typing import Optional

# -------------------------------------------
# OrderBase
# Define los campos comunes que comparten todas las órdenes.
# -------------------------------------------
class OrderBase(BaseModel):
    cliente: str
    dron: str
    descripcion: str
    estado: str
    fecha_ingreso: str
    fecha_entrega: Optional[str] = None  # Puede ser nulo

# -------------------------------------------
# OrderUpdate
# Permite actualizar uno o varios campos de la orden.
# Todos los campos son opcionales para actualizaciones parciales.
# -------------------------------------------
class OrderUpdate(BaseModel):
    cliente: Optional[str] = None
    dron: Optional[str] = None
    descripcion: Optional[str] = None
    estado: Optional[str] = None
    fecha_ingreso: Optional[str] = None
    fecha_entrega: Optional[str] = None

# -------------------------------------------
# OrderCreate
# Extiende OrderBase, se usa cuando el cliente crea una orden.
# En este caso no agregamos nada nuevo, pero permite separar responsabilidades.
# -------------------------------------------
class OrderCreate(OrderBase):
    pass

# -------------------------------------------
# Order
# Esquema completo que representa una orden con ID.
# Se usa como respuesta de la API.
# -------------------------------------------
class Order(OrderBase):
    id: int  # Se agrega el campo ID que viene de la DB

    class Config:
        orm_mode = True
        # orm_mode = True permite que Pydantic trabaje directamente
        # con objetos de SQLAlchemy en lugar de requerir dicts.
