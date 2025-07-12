from fastapi import FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse
from sqlalchemy.orm import Session

from .routes import router
from .db import get_db
from .models import Problem

app = FastAPI()
app.include_router(router)

templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request, db: Session = Depends(get_db)):
    problems = db.query(Problem).order_by(Problem.id.desc()).all()
    return templates.TemplateResponse(
        "index.html", {"request": request, "problems": problems}
    )
