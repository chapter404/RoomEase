from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from database.connection import Base


class Reserva(Base):
    __tablename__ = "Reserva"

    idReserva = Column(Integer, primary_key=True, index=True)
    fechaInicio = Column(Date, nullable=False)
    fechaFin = Column(Date, nullable=False)
    estado = Column(String(50), nullable=False, default="pendiente")
    clienteId = Column(Integer, ForeignKey("Cliente.idCliente", ondelete="CASCADE"), nullable=False)

    cliente = relationship("Cliente", back_populates="reservas")
    habitaciones = relationship("ReservaHabitacion", back_populates="reserva", cascade="all, delete-orphan")


class ReservaHabitacion(Base):
    __tablename__ = "Reserva_Habitacion"

    idReservaHabitacion = Column(Integer, primary_key=True, index=True)
    reservaId = Column(Integer, ForeignKey("Reserva.idReserva", ondelete="CASCADE"), nullable=False)
    habitacionId = Column(Integer, ForeignKey("Habitacion.idHabitacion", ondelete="CASCADE"), nullable=False)

    reserva = relationship("Reserva", back_populates="habitaciones")
    habitacion = relationship("Habitacion", back_populates="reservas")