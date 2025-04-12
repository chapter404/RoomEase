from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session
from database.connection import get_db
from models.user import Cliente
from utils.hashing import hash_password

router = APIRouter()

class RegisterRequest(BaseModel):
    nombre: str
    rut: int
    dv: str
    telefono: int
    correo: EmailStr
    password: str

@router.post("/register")
def registrar_usuario(request: RegisterRequest, db: Session = Depends(get_db)):
    usuario_existente = db.query(Cliente).filter(Cliente.correo == request.correo).first()
    if usuario_existente:
        raise HTTPException(status_code=400, detail="El correo ya está registrado")

    rut_existente = db.query(Cliente).filter(Cliente.rut == request.rut, Cliente.dv == request.dv).first()
    if rut_existente:
        raise HTTPException(status_code=400, detail="El RUT ya está registrado")

    hashed_password = hash_password(request.password)
    nuevo_cliente = Cliente(
        nombre=request.nombre,
        rut=request.rut,
        dv=request.dv,
        telefono=request.telefono,
        correo=request.correo,
        password=hashed_password
    )
    db.add(nuevo_cliente)
    db.commit()
    db.refresh(nuevo_cliente)
    return {"idCliente": nuevo_cliente.idCliente, "nombre": nuevo_cliente.nombre, "correo": nuevo_cliente.correo}