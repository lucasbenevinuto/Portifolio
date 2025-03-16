from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="templates")

# Sample project data - in a real application, this would come from a database
projects = [
    {
        "id": 1,
        "title": "Machine Learning Fraud Detection",
        "description": "Developed a machine learning model to detect fraudulent transactions with 99.5% accuracy, resulting in a 75% reduction in fraud-related losses.",
        "image": "images/project1.jpg",
        "category": "Machine Learning",
        "github": "https://github.com/yourusername/fraud-detection",
        "demo": "https://demo.yourdomain.com/fraud-detection"
    },
    {
        "id": 2,
        "title": "Natural Language Processing for Customer Service",
        "description": "Built an NLP system that automatically routes customer queries to the right department with 95% accuracy, reducing response time by 50%.",
        "image": "images/project2.jpg",
        "category": "Natural Language Processing",
        "github": "https://github.com/yourusername/nlp-customer-service",
        "demo": "https://demo.yourdomain.com/nlp-service"
    },
    {
        "id": 3,
        "title": "Computer Vision for Retail Analytics",
        "description": "Created a computer vision system that analyzes customer flow in retail stores, providing insights that increased conversion rates by 25%.",
        "image": "images/project3.jpg",
        "category": "Computer Vision",
        "github": "https://github.com/yourusername/retail-vision",
        "demo": "https://demo.yourdomain.com/retail-vision"
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