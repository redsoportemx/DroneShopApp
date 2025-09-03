# Importamos las librerías necesarias
from fastapi import FastAPI, HTTPException     # FastAPI para crear la API, HTTPException para manejar errores
from pydantic import BaseModel                 # BaseModel nos ayuda a definir modelos de datos (validación automática)
from typing import List, Optional              # Para listas y valores opcionales

# Inicializamos la aplicación FastAPI
app = FastAPI()

# Definimos el modelo de datos para una orden de servicio
class Order(BaseModel):
    id: int                        # Identificador único de la orden
    cliente: str                   # Nombre del cliente
    dron: str                      # Modelo del dron
    descripcion: str               # Descripción del problema
    estado: str                    # Estado actual de la orden (pendiente, en proceso, terminado, entregado)
    fecha_ingreso: str             # Fecha en la que se registró la orden
    fecha_entrega: Optional[str] = None  # Fecha de entrega (puede ser nula)

# "Base de datos" en memoria (solo lista de órdenes para pruebas rápidas)
db: List[Order] = []

# -------------------------------
# Crear nueva orden (CREATE)
# -------------------------------
@app.post("/orders/")
def crear_orden(order: Order):
    db.append(order)  # Se agrega la orden a la lista en memoria
    return {"mensaje": "Orden creada", "orden": order}

# -------------------------------
# Listar todas las órdenes (READ)
# -------------------------------
@app.get("/orders/")
def listar_ordenes():
    return db   # Retorna todas las órdenes guardadas en memoria

# -------------------------------
# Consultar una orden por ID (READ ONE)
# -------------------------------
@app.get("/orders/{order_id}")
def obtener_orden(order_id: int):
    for orden in db:                       # Recorremos todas las órdenes en la "db"
        if orden.id == order_id:           # Comparamos: si el id de la orden coincide con el ID pasado en el endpoint
            return orden                   # Retorna la orden encontrada
    raise HTTPException(status_code=404, detail="Orden no encontrada")  # Si no existe, error 404

# -------------------------------
# Actualizar toda la orden (UPDATE - PUT)
# -------------------------------
@app.put("/orders/{order_id}")
def actualizar_orden(order_id: int, nueva_orden: Order):
    for i, orden in enumerate(db):         # enumerate da índice (i) y objeto (orden)
        if orden.id == order_id:           # Si encontramos la orden con el mismo ID
            db[i] = nueva_orden            # Reemplazamos la orden completa
            return {"mensaje": "Orden reemplazada", "orden": nueva_orden}
    raise HTTPException(status_code=404, detail="Orden no encontrada")

# -------------------------------
# Actualizar SOLO el estado (UPDATE - PATCH)
# -------------------------------
@app.patch("/orders/{order_id}")
def actualizar_estado(order_id: int, estado: str):
    for orden in db:
        # 👉 Explicación clara de tu duda:
        # orden.id → es el campo del objeto guardado en la "base de datos" (lista db).
        # order_id → es el parámetro que viene desde la URL del endpoint.
        # Ejemplo: PATCH /orders/3 → order_id = 3
        # Entonces: si el id de la orden (orden.id) es igual al ID solicitado (order_id), significa que encontramos la orden correcta.
        if orden.id == order_id:
            orden.estado = estado  # Solo modificamos el campo estado
            return {"mensaje": "Estado actualizado", "orden": orden}
    raise HTTPException(status_code=404, detail="Orden no encontrada")

# -------------------------------
# Eliminar una orden (DELETE)
# -------------------------------
@app.delete("/orders/{order_id}")
def eliminar_orden(order_id: int):
    for i, orden in enumerate(db):
        if orden.id == order_id:
            db.pop(i)  # Eliminamos la orden por índice
            return {"mensaje": f"Orden {order_id} eliminada"}
    raise HTTPException(status_code=404, detail="Orden no encontrada")
