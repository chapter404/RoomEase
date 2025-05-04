from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from routers import login, register, habitacion
from routers.reserva import router as reserva_router

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:4200",
    "http://127.0.0.1",
    "http://127.0.0.1:4200",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

app.include_router(login.router)
app.include_router(register.router)
app.include_router(habitacion.router)
app.include_router(reserva_router)

@app.get("/")
async def root():
    return {"message": "Bienvenido a RoomEase"}
