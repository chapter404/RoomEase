# backend/src/routers/reserva.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import pymysql

# Creamos un APIRouter para agrupar todas las rutas relacionadas con reservas
router = APIRouter(prefix="/reservas", tags=["reservas"])

# Definimos el esquema de datos que recibiremos desde el frontend con Pydantic
class ReservaRequest(BaseModel):
    fechaInicio: str      # Fecha de inicio de la reserva en formato 'YYYY-MM-DD'
    fechaFin: str         # Fecha de fin de la reserva en formato 'YYYY-MM-DD'
    habitacionId: int     # ID de la habitación que se desea reservar
    clienteId: int        # ID del cliente que realiza la reserva

# Configuración de la conexión a la base de datos MySQL usando PyMySQL
conexion = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    database="RoomEase",
    cursorclass=pymysql.cursors.DictCursor  # Para obtener resultados como diccionarios
)

@router.post("/", summary="Crear una nueva reserva")
def crear_reserva(reserva: ReservaRequest):
    """
    Endpoint que recibe los datos de una reserva, los inserta en la tabla Reserva,
    relaciona la reserva con una habitación en Reserva_Habitacion y devuelve
    el ID de la nueva reserva.
    """
    try:
        # Abrimos un cursor para ejecutar comandos SQL
        with conexion.cursor() as cursor:
            # 1) Insertar la reserva en la tabla Reserva
            sql_reserva = (
                """
                INSERT INTO Reserva (fechaInicio, fechaFin, estado, clienteId)
                VALUES (%s, %s, %s, %s)
                """
            )
            valores_reserva = (
                reserva.fechaInicio,
                reserva.fechaFin,
                "pendiente",      # Estado inicial de la reserva
                reserva.clienteId
            )
            cursor.execute(sql_reserva, valores_reserva)

            # Obtenemos el ID generado automáticamente por la tabla Reserva
            reserva_id = cursor.lastrowid

            # 2) Insertar la relación en Reserva_Habitacion
            sql_reserva_habitacion = (
                """
                INSERT INTO Reserva_Habitacion (reservaId, habitacionId)
                VALUES (%s, %s)
                """
            )
            valores_reserva_habitacion = (
                reserva_id,
                reserva.habitacionId
            )
            cursor.execute(sql_reserva_habitacion, valores_reserva_habitacion)

            # 3) Confirmar los cambios en la base de datos
            conexion.commit()

        # Devolver la respuesta exitosa con el ID de la reserva creada
        return {"mensaje": "Reserva creada exitosamente", "reservaId": reserva_id}

    except Exception as e:
        # Si ocurre un error, revertimos la transacción
        conexion.rollback()
        # Lanzamos una excepción HTTP 500 con el detalle del error
        raise HTTPException(status_code=500, detail=f"Error al crear reserva: {e}")
