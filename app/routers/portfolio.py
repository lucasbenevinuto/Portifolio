from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter(tags=["portfolio"])

templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html", 
        {"request": request, "active_page": "home"}
    )

@router.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse(
        "about.html", 
        {"request": request, "active_page": "about"}
    )

@router.get("/skills", response_class=HTMLResponse)
async def skills(request: Request):
    return templates.TemplateResponse(
        "skills.html", 
        {"request": request, "active_page": "skills"}
    )

@router.get("/contact", response_class=HTMLResponse)
async def contact(request: Request):
    return templates.TemplateResponse(
        "contact.html", 
        {"request": request, "active_page": "contact"}
    ) 