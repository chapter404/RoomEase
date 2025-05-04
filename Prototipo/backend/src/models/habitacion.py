from sqlalchemy import Column, Integer, String, Enum, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from database.connection import Base


class Habitacion(Base):
    __tablename__ = "Habitacion"

    idHabitacion = Column(Integer, primary_key=True, index=True)
    numero = Column(String(10), unique=True, nullable=False)
    tipo = Column(String(100), nullable=False)
    precio = Column(Integer, nullable=False)
    estado = Column(Enum("disponible", "ocupada", "mantenimiento"), nullable=False)
    descripcion = Column(Text, nullable=True)

    fotos = relationship("FotoHabitacion", back_populates="habitacion", cascade="all, delete-orphan")
    reservas = relationship("ReservaHabitacion", back_populates="habitacion", cascade="all, delete-orphan")

class FotoHabitacion(Base):
    __tablename__ = "FotoHabitacion"

    idFoto = Column(Integer, primary_key=True, index=True)
    habitacionId = Column(Integer, ForeignKey("Habitacion.idHabitacion", ondelete="CASCADE"), nullable=False)
    urlFoto = Column(String(255), nullable=False)
    descripcionFoto = Column(String(255), nullable=True)
    orden = Column(Integer, nullable=True)

    habitacion = relationship("Habitacion", back_populates="fotos")