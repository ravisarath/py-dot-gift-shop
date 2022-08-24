from ast import operator
from unittest import result
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .schemas import Items, BlogCreate
from .utils import Operations
from .database import get_db
from .models import Blogs

router = APIRouter(prefix="/api")


@router.post("/blog/")
def create_blog(request: BlogCreate, db: Session = Depends(get_db)):
    new_blog = Blogs(id = request.id, message = request.message )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@router.get("all")
def get_blog(db: Session = Depends(get_db)):
    return db.query(Blogs).all()

@router.post("/math")
def math_operation(item: Items) -> int:
    operator = Operations(item.first, item.second)
    result = operator.addition()
    return result

@router.post("/sum")
def math_operation(item: Items) -> int:
    operator = Operations(item.first, item.second)
    result = operator.multiply    
    return result
