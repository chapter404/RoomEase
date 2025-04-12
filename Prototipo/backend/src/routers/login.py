from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database.connection import get_db
from services.auth import authenticate_user

router = APIRouter()

class LoginRequest(BaseModel):
    correo: str
    password: str

@router.post("/login")
def login(request: LoginRequest, db: Session = Depends(get_db)):

    user = authenticate_user(db, request.correo, request.password)
    
    if not user:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    
    return {"message": "Inicio de sesión exitoso", "user": {"id": user.idCliente, "correo": user.correo}}