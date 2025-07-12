from fastapi import APIRouter, Request, Form, Depends
from sqlalchemy.orm import Session
from .db import get_db
from .models import Problem

router = APIRouter()


@router.post("/add")
def add_problem(statement: str = Form(...), db: Session = Depends(get_db)):
    problem = Problem(statement=statement)
    db.add(problem)
    db.commit()
    return {"status": "ok"}
