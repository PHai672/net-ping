import csv
from .database import SessionLocal
from . import crud, models, schemas

def import_csv(filepath: str = "branches.csv"):
    db = SessionLocal()
    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            crud.create_branch(db, name=row['branch_name'], ip=row['ip'])
    db.close()

if __name__ == "__main__":
    import_csv()
