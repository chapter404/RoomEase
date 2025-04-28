from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
import pymysql

from routers import login, register, habitacion
from routers.reserva import router as reserva_router

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(login.router)
app.include_router(register.router)
app.include_router(habitacion.router)
app.include_router(reserva_router)

# Global database connection
conexion = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    database="RoomEase",
    cursorclass=pymysql.cursors.DictCursor
)

# Seeder: populates initial data in development
@app.on_event("startup")
def seed_database():
    # Only seed in development environment
    if os.getenv("ENV", "dev") == "dev":
        with conexion.cursor() as cursor:
            # Seed a test client if none exists
            cursor.execute("SELECT COUNT(*) AS cnt FROM Cliente")
            if cursor.fetchone()["cnt"] == 0:
                cursor.execute("""
                    INSERT INTO Cliente 
                      (nombre, rut, dv, telefono, correo, password)
                    VALUES
                      ('Cliente Prueba',12345678,'K',987654321,'prueba@example.com','pass123')
                """)
            # Seed test rooms if none exist
            cursor.execute("SELECT COUNT(*) AS cnt FROM Habitacion")
            if cursor.fetchone()["cnt"] == 0:
                cursor.execute("""
                    INSERT INTO Habitacion
                      (numero, tipo, precio, estado, descripcion)
                    VALUES
                      ('101','Individual',30000,'disponible','Cama sencilla'),
                      ('102','Doble',     45000,'disponible','Dos camas'),
                      ('103','Suite',     60000,'disponible','Cama king size y sala')
                """)
            conexion.commit()

@app.get("/")
async def main():
    return {"message": "Bienvenido a RoomEase"}
