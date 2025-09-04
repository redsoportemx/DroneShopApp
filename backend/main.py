# Importamos FastAPI para crear la API, Depends para inyectar dependencias
# y HTTPException para manejar errores en caso de que algo falle.
from fastapi import FastAPI, Depends, HTTPException

# Importamos Session para manejar las conexiones a la base de datos con SQLAlchemy.
from sqlalchemy.orm import Session

# Importamos BaseModel de Pydantic, que nos permite definir el esquema
# de los datos que se reciben en el body (JSON) de las peticiones.
from pydantic import BaseModel

# Importamos nuestros módulos locales: modelos, esquemas y la conexión a la DB.
import models
import schemas
import database


# Instanciamos la aplicación FastAPI.
app = FastAPI()

# -------------------------------------------
# Crear tablas en la base de datos si no existen.
# Esto se hace a partir de los modelos definidos en models.py
# usando la "Base" que declaramos en database.py
# -------------------------------------------
models.Base.metadata.create_all(bind=database.engine)

# -------------------------------------------
# Dependencia get_db()
# Esta función abre una sesión con la base de datos cada vez que se hace
# una petición y la cierra al terminar.
# -------------------------------------------
def get_db():
    db = database.SessionLocal()  # Abrimos la conexión
    try:
        yield db                   # La función "cede" la conexión a quien la necesite
    finally:
        db.close()                 # Al terminar, cerramos la conexión


# -------------------------------------------
# Crear una nueva orden (POST /orders/)
# Recibe un objeto OrderCreate (definido en schemas.py).
# Guarda la nueva orden en la base de datos.
# -------------------------------------------
@app.post("/orders/", response_model=schemas.Order)
def crear_orden(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    # Creamos una nueva instancia del modelo Order usando los datos recibidos
    nueva_orden = models.Order(**order.dict())
    
    # Agregamos la nueva orden a la sesión de DB
    db.add(nueva_orden)
    db.commit()              # Guardamos los cambios en la DB
    db.refresh(nueva_orden)  # Refrescamos para obtener el objeto con su ID asignado
    return nueva_orden       # Devolvemos la orden recién creada


# -------------------------------------------
# Listar todas las órdenes (GET /orders/)
# Retorna todas las órdenes que hay en la base de datos.
# -------------------------------------------
@app.get("/orders/", response_model=list[schemas.Order])
def listar_ordenes(db: Session = Depends(get_db)):
    # Hacemos una consulta SQLAlchemy para obtener todas las órdenes
    return db.query(models.Order).all()


# -------------------------------------------
# Modelo para actualizar el estado de una orden
# Usamos BaseModel de Pydantic para validar que el body JSON
# contenga un campo "estado" de tipo string.
# -------------------------------------------
class EstadoUpdate(BaseModel):
    estado: str


# -------------------------------------------
# Actualizar solo el estado de una orden (PATCH /orders/{order_id})
# Recibe el ID de la orden en la URL y el nuevo estado en el body (JSON).
# -------------------------------------------
@app.patch("/orders/{order_id}", response_model=schemas.Order)
def actualizar_estado(order_id: int, data: EstadoUpdate, db: Session = Depends(get_db)):
    # Buscamos la orden en la DB filtrando por ID
    orden = db.query(models.Order).filter(models.Order.id == order_id).first()

    # Si no se encuentra la orden, devolvemos error 404
    if not orden:
        raise HTTPException(status_code=404, detail="Orden no encontrada")

    # Si se encontró, actualizamos el estado usando el body recibido
    orden.estado = data.estado
    db.commit()          # Guardamos cambios
    db.refresh(orden)    # Refrescamos el objeto para devolverlo actualizado
    return orden


# -------------------------------------------
# Eliminar una orden (DELETE /orders/{order_id})
# Recibe el ID de la orden en la URL.
# Elimina la orden de la base de datos si existe.
# -------------------------------------------
@app.delete("/orders/{order_id}")
def eliminar_orden(order_id: int, db: Session = Depends(get_db)):
    # Buscamos la orden por ID
    orden = db.query(models.Order).filter(models.Order.id == order_id).first()

    # Si no existe, devolvemos error 404
    if not orden:
        raise HTTPException(status_code=404, detail="Orden no encontrada")

    # Si existe, la eliminamos
    db.delete(orden)
    db.commit()  # Guardamos cambios en la DB
    return {"mensaje": f"Orden con ID {order_id} eliminada correctamente"}
