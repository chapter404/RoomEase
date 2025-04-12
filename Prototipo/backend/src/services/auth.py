from sqlalchemy.orm import Session
from models.user import Cliente
from utils.hashing import verify_password

def authenticate_user(db: Session, correo: str, password: str):
    user = db.query(Cliente).filter(Cliente.correo == correo).first()
    
    if not user:
        return None
    
    if not verify_password(password, user.password):
        return None
    
    return user