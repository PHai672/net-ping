from pydantic import BaseModel

class BranchBase(BaseModel):
    branch_name: str
    ip: str

class BranchCreate(BranchBase):
    pass

class Branch(BranchBase):
    id: int

    class Config:
        orm_mode = True
