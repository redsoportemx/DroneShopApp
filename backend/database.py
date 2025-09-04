import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Leer la URL desde las variables de entorno que definiste en docker-compose.yml
DATABASE_URL = os.getenv("DATABASE_URL")

# Crear el motor de conexión a la base de datos
engine = create_engine(DATABASE_URL)

# Sesión de conexión que usaremos en los endpoints
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para los modelos
Base = declarative_base()
