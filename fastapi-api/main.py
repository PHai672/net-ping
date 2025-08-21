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

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # หรือระบุ IP frontend ก็ได้
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
