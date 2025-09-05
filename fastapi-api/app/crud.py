from sqlalchemy.orm import Session
from . import models, schemas

def get_branches(db: Session):
    return db.query(models.Branch).all()

def create_branch(db: Session, name: str, ip: str):
    db_branch = models.Branch(branch_name=name, ip=ip)
    db.add(db_branch)
    db.commit()
    db.refresh(db_branch)
    return db_branch
