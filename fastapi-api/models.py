from pydantic import BaseModel

class Branch(BaseModel):
    ip: str
    branch_name: str
