from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from datetime import datetime

router = APIRouter()

templates = Jinja2Templates(directory="templates")

# Medium articles to be featured in the blog section
blog_posts = [
    {
        "id": 1,
        "title": "SVMs: Teoria e Prática",
        "summary": "Um artigo sobre Support Vector Machines, explicando os conceitos teóricos e aplicações práticas.",
        "url": "https://medium.com/@lucasbenevinutopereira/svms-teoria-e-prática-ee741e544080",
        "date": datetime(2024, 3, 10),
        "author": "Lucas Benevinuto",
        "tags": ["Machine Learning", "SVMs", "Classificação"]
    },
    {
        "id": 2,
        "title": "Funções de Custo em Machine Learning: Uma Visão Abrangente",
        "summary": "Uma análise detalhada das diferentes funções de custo utilizadas em modelos de machine learning.",
        "url": "https://medium.com/@lucasbenevinutopereira/funções-de-custo-em-machine-learning-uma-visão-abrangente-7cd95ba1058e",
        "date": datetime(2024, 3, 5),
        "author": "Lucas Benevinuto",
        "tags": ["Machine Learning", "Funções de Custo", "Otimização"]
    },
    {
        "id": 3,
        "title": "Destrinchando Vetores",
        "summary": "Uma explicação aprofundada sobre vetores e suas aplicações em álgebra linear e machine learning.",
        "url": "https://medium.com/@lucasbenevinutopereira/destrinchando-vetores-963b1ec954ec",
        "date": datetime(2024, 2, 25),
        "author": "Lucas Benevinuto",
        "tags": ["Matemática", "Álgebra Linear", "Vetores"]
    },
    {
        "id": 4,
        "title": "Regressão Linear em Machine Learning",
        "summary": "Um guia completo sobre regressão linear e sua implementação em problemas de machine learning.",
        "url": "https://medium.com/@lucasbenevinutopereira/regressão-linear-em-machine-learning-bfebc4fe5969",
        "date": datetime(2024, 2, 20),
        "author": "Lucas Benevinuto",
        "tags": ["Machine Learning", "Regressão Linear", "Estatística"]
    },
    {
        "id": 5,
        "title": "Destrinchando a Regressão Linear",
        "summary": "Uma análise detalhada dos fundamentos matemáticos e estatísticos por trás da regressão linear.",
        "url": "https://medium.com/@lucasbenevinutopereira/destrinchando-a-regressão-linear-aae2847351db",
        "date": datetime(2024, 2, 15),
        "author": "Lucas Benevinuto",
        "tags": ["Machine Learning", "Regressão Linear", "Modelagem"]
    },
    {
        "id": 6,
        "title": "Fundamentos SQL",
        "summary": "Um guia prático sobre os fundamentos da linguagem SQL para manipulação e consulta de dados.",
        "url": "https://medium.com/@lucasbenevinutopereira/fundamentos-sql-654f39b67a7c",
        "date": datetime(2024, 2, 10),
        "author": "Lucas Benevinuto",
        "tags": ["SQL", "Bancos de Dados", "Análise de Dados"]
    },
    {
        "id": 7,
        "title": "Introdução a Machine Learning",
        "summary": "Uma introdução aos conceitos fundamentais de machine learning e suas aplicações.",
        "url": "https://medium.com/@lucasbenevinutopereira/introdução-a-machine-learning-d91dec8f7964",
        "date": datetime(2024, 2, 5),
        "author": "Lucas Benevinuto",
        "tags": ["Machine Learning", "Data Science", "IA"]
    }
]

@router.get("/", response_class=HTMLResponse)
async def get_blog_posts(request: Request):
    return templates.TemplateResponse(
        "blog.html", 
        {"request": request, "posts": blog_posts, "active_page": "blog"}
    )

@router.get("/{post_id}", response_class=HTMLResponse)
async def get_blog_post(request: Request, post_id: int):
    post = next((p for p in blog_posts if p["id"] == post_id), None)
    if not post:
        return templates.TemplateResponse(
            "404.html", 
            {"request": request}, 
            status_code=404
        )
    # Redirect to Medium article
    return templates.TemplateResponse(
        "blog_redirect.html", 
        {"request": request, "post": post, "active_page": "blog"}
    ) 