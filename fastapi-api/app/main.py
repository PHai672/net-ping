from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency สำหรับใช้งาน DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/branches", response_model=list[schemas.Branch])
def read_branches(db: Session = Depends(get_db)):
    return crud.get_branches(db)

@app.post("/branches", response_model=schemas.Branch)
def create_branch(branch: schemas.BranchCreate, db: Session = Depends(get_db)):
    return crud.create_branch(db, branch)
