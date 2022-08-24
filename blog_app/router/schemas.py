from email import message
from fastapi import  HTTPException
from pydantic import BaseModel, validator

class Items(BaseModel):
    first: int
    second: int
    operation_type:str = "sum"


class BlogCreate(BaseModel):
    id: int
    message: str