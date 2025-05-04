from fastapi import APIRouter, Depends, UploadFile, File, Form
from sqlalchemy.orm import Session
from models.habitacion import Habitacion, FotoHabitacion
from database.connection import get_db
import os
from uuid import uuid4
import logging

logging.basicConfig(level=logging.INFO)

router = APIRouter(prefix="/habitaciones", tags=["Habitaciones"])

UPLOAD_DIR = "uploads"

@router.post("/")
async def crear_habitacion(
    numero: str = Form(...),
    tipo: str = Form(...),
    precio: int = Form(...),
    estado: str = Form(...),
    descripcion: str = Form(None),
    fotos: list[UploadFile] = File(...),
    db: Session = Depends(get_db)
):
    if not os.path.exists(UPLOAD_DIR):
        os.makedirs(UPLOAD_DIR)

    nueva_habitacion = Habitacion(
        numero=numero,
        tipo=tipo,
        precio=precio,
        estado=estado,
        descripcion=descripcion
    )
    db.add(nueva_habitacion)
    db.commit()
    db.refresh(nueva_habitacion)

    for index, foto in enumerate(fotos):
        extension = foto.filename.split(".")[-1]
        nombre_archivo = f"{uuid4()}.{extension}"
        ruta_archivo = os.path.join(UPLOAD_DIR, nombre_archivo)

        with open(ruta_archivo, "wb") as f:
            f.write(await foto.read())

        nueva_foto = FotoHabitacion(
            habitacionId=nueva_habitacion.idHabitacion,
            urlFoto=ruta_archivo,
            orden=index
        )
        db.add(nueva_foto)

    db.commit()
    logging.info(f"Habitación creada con éxito: ID {nueva_habitacion.idHabitacion}")
    return {"message": "Habitación creada con éxito", "idHabitacion": nueva_habitacion.idHabitacion}

@router.get("")
def listar_habitaciones(db: Session = Depends(get_db)):
    habitaciones = db.query(Habitacion).all()
    resultado = []
    for habitacion in habitaciones:
        fotos = db.query(FotoHabitacion).filter(FotoHabitacion.habitacionId == habitacion.idHabitacion).all()
        fotos_urls = [f"http://localhost:8000/{foto.urlFoto}" for foto in fotos]
        resultado.append({
            "idHabitacion": habitacion.idHabitacion,
            "numero": habitacion.numero,
            "tipo": habitacion.tipo,
            "precio": habitacion.precio,
            "estado": habitacion.estado,
            "descripcion": habitacion.descripcion,
            "fotos": fotos_urls
        })
    return resultado