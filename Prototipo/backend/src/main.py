from fastapi import FastAPI
from routers import login, register
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(login.router)
app.include_router(register.router)

@app.get("/")
async def root():
    return {"message": "Bienvenido a RoomEase"}