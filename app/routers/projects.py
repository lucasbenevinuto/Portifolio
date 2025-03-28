from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="templates")

# Sample project data - in a real application, this would come from a database
projects = [
    {
        "id": 1,
        "title": "Análise Imobiliária EUA",
        "description": "Este projeto tem como objetivo analisar imóveis para aluguel nos Estados Unidos, com foco na identificação das comodidades mais relevantes para o preço e localização de maior valor. Através de técnicas de Machine Learning, segmentação de mercado e análise de padrões, foi possível gerar insights valiosos sobre o comportamento do mercado imobiliário.",
        "image": "/static/images/project1.jpg",
        "category": "Machine Learning",
        "technologies": ["Python", "Machine Learning", "Análise de Dados"],
        "github": "https://github.com/lucasbenevinuto/Real-Estate-Analysis-with-Machine-Learning",
        "demo": "",
        "period": "set de 2024 - out de 2024"
    },
    {
        "id": 2,
        "title": "Financial Loan Risk Assessment and Approval Prediction",
        "description": "O projeto Financial Loan Risk Assessment and Approval Prediction consiste no desenvolvimento de modelos preditivos para avaliar o risco de empréstimos e prever a probabilidade de aprovação, utilizando um dataset sintético com variáveis financeiras e comportamentais dos clientes.",
        "image": "/static/images/project2.jpg",
        "category": "Machine Learning",
        "technologies": ["Python", "Machine Learning", "Análise de Risco"],
        "github": "https://github.com/lucasbenevinuto/Risk-Analysis",
        "demo": "",
        "period": "set de 2024 - out de 2024"
    }
]

@router.get("/", response_class=HTMLResponse)
async def get_projects(request: Request):
    return templates.TemplateResponse(
        "projects.html", 
        {"request": request, "projects": projects, "active_page": "projects"}
    )

@router.get("/{project_id}", response_class=HTMLResponse)
async def get_project(request: Request, project_id: int):
    project = next((p for p in projects if p["id"] == project_id), None)
    if not project:
        return templates.TemplateResponse(
            "404.html", 
            {"request": request}, 
            status_code=404
        )
    return templates.TemplateResponse(
        "project_detail.html", 
        {"request": request, "project": project, "active_page": "projects"}
    ) 