from sqlalchemy import Column, Integer, String, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from database.connection import Base


class Cliente(Base):
    __tablename__ = "Cliente"

    idCliente = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    rut = Column(Integer, nullable=False)
    dv = Column(String(1), nullable=False)
    telefono = Column(Integer, nullable=True)
    correo = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)

    reservas = relationship("Reserva", back_populates="cliente", cascade="all, delete-orphan")
    __table_args__ = (UniqueConstraint('rut', 'dv', name='uq_rut_dv'),)