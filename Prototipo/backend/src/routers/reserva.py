from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database.connection import get_db
from models.reserva import Reserva, ReservaHabitacion

router = APIRouter(prefix="/reservas", tags=["reservas"])

class ReservaRequest(BaseModel):
    fechaInicio: str
    fechaFin: str
    habitacionId: int
    clienteId: int

@router.post("/", summary="Crear una nueva reserva")
def crear_reserva(reserva: ReservaRequest, db: Session = Depends(get_db)):
    try:
        nueva_reserva = Reserva(
            fechaInicio=reserva.fechaInicio,
            fechaFin=reserva.fechaFin,
            estado="pendiente",
            clienteId=reserva.clienteId
        )
        db.add(nueva_reserva)
        db.commit()
        db.refresh(nueva_reserva)

        nueva_reserva_habitacion = ReservaHabitacion(
            reservaId=nueva_reserva.idReserva,
            habitacionId=reserva.habitacionId
        )
        db.add(nueva_reserva_habitacion)
        db.commit()

        return {"mensaje": "Reserva creada exitosamente", "reservaId": nueva_reserva.idReserva}

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al crear reserva: {e}")