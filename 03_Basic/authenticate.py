from fastapi import Depends, HTTPException
from fastapi.security import (
    HTTPBasic,
    HTTPBasicCredentials)
import crud
from database import SessionLocal, engine

security = HTTPBasic()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


async def authenticate_user(
        db: SessionLocal = Depends(get_db),
        credentials: HTTPBasicCredentials = Depends(security)):
    if crud.authenticate_user_crud(db,
                              credentials.username,
                              credentials.password):
        return True
    else:
        raise HTTPException(
            status_code=401,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"})
