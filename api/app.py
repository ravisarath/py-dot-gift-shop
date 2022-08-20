from fastapi import FastAPI
from blog_app.utils import Operations
from blog_app.api.schemas import Addition

app = FastAPI()

# crud operation get post put delete

@app.get("/")
def test_api():
    return {"message":"success"}

@app.post("/sum")
def sum_api(a:Addition) -> int: 
    """
    add given 2 number
    param: a int, b int
    return: sum int
    """
    operatorion = Operations(a.first,a.second)
    sum = operatorion.addition()
    return sum

