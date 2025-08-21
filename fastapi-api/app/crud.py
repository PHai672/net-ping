from sqlalchemy.orm import Session
import models, schemas

def get_branches(db: Session):
    return db.query(models.Branch).all()

def create_branch(db: Session, branch: schemas.BranchCreate):
    db_branch = models.Branch(branch_name=branch.branch_name, ip=branch.ip)
    db.add(db_branch)
    db.commit()
    db.refresh(db_branch)
    return db_branch
