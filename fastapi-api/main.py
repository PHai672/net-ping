from fastapi import FastAPI, HTTPException
from models import Branch
import crud

app = FastAPI()

@app.get("/branches")
def get_branches():
    return crud.read_all_branches()

@app.post("/branches")
def create_branch(branch: Branch):
    try:
        crud.add_branch(branch)
        return {"message": "Branch added"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.put("/branches/{ip}")
def update_branch(ip: str, branch: Branch):
    try:
        crud.update_branch(ip, branch)
        return {"message": "Branch updated"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.delete("/branches/{ip}")
def delete_branch(ip: str):
    try:
        crud.delete_branch(ip)
        return {"message": "Branch deleted"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
