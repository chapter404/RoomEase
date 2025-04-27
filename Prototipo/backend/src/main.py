from fastapi import FastAPI
from routers import login, register, habitacion
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(login.router)
app.include_router(register.router)
app.include_router(habitacion.router)

@app.get("/")
async def main():
    return {"message": "Bienvenido a RoomEase"}