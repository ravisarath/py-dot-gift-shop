from pydantic import BaseModel

class Addition(BaseModel):
    first: int
    second: int
