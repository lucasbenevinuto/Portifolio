from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, PlainTextResponse
from starlette.middleware.base import BaseHTTPMiddleware
from app.routers import portfolio, projects, blog
import uvicorn
import logging
import os
import re
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class CSPMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        if isinstance(response, HTMLResponse):
            response.headers["Content-Security-Policy"] = "default-src 'self'; script-src 'self' 'unsafe-inline' 'unsafe-eval' https://cdnjs.cloudflare.com; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com https://cdnjs.cloudflare.com data:; font-src 'self' https://fonts.gstatic.com https://cdnjs.cloudflare.com data:; img-src 'self' data:;"
        return response

# Middleware para controle de cache
class CacheControlMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        if request.url.path.startswith("/static"):
            response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
            response.headers["Pragma"] = "no-cache"
            response.headers["Expires"] = "0"
        return response

# Middleware para logging de requisições
class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        logger.debug(f"Request path: {request.url.path}")
        response = await call_next(request)
        logger.debug(f"Response status: {response.status_code}")
        return response

app = FastAPI(
    title="Data Science & AI Portfolio",
    description="Portfolio website for a Data Scientist and AI Engineer",
    version="1.0.0"
)

# Add logging middleware
app.add_middleware(LoggingMiddleware)

# Add CSP middleware
app.add_middleware(CSPMiddleware)

# Add cache control middleware
app.add_middleware(CacheControlMiddleware)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create test.css file
test_css = """
body {
    font-family: Arial, sans-serif;
    color: blue;
    background-color: #f0f0f0;
}
h1 {
    color: #4A6CF7;
    font-size: 2.5rem;
}
.container {
    width: 100%;
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
}
"""

test_css_path = os.path.join("static", "css", "test.css")
os.makedirs(os.path.dirname(test_css_path), exist_ok=True)
with open(test_css_path, "w") as f:
    f.write(test_css)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Include routers
app.include_router(portfolio.router)
app.include_router(projects.router, prefix="/projects", tags=["projects"])
app.include_router(blog.router, prefix="/blog", tags=["blog"])

# Rota para debug - verificar se conseguimos acessar arquivos estáticos diretamente
@app.get("/debug/css", tags=["debug"])
async def debug_css():
    logger.debug("Debug CSS route accessed")
    try:
        with open("static/css/styles.css", "r") as f:
            return {"css_exists": True, "first_few_lines": f.read(500)}
    except Exception as e:
        logger.error(f"Error accessing CSS: {str(e)}")
        return {"css_exists": False, "error": str(e)}

# Rota para CSS de teste simples
@app.get("/static/css/simple.css", response_class=PlainTextResponse)
async def simple_css():
    return """
    body { color: blue; font-family: Arial; }
    h1 { color: red; }
    .container { width: 80%; margin: 0 auto; }
    """

def setup_directories():
    """Garantir que todas as pastas necessárias existam."""
    os.makedirs(os.path.join("static", "css"), exist_ok=True)
    os.makedirs(os.path.join("static", "js"), exist_ok=True)
    os.makedirs(os.path.join("static", "images"), exist_ok=True)
    os.makedirs(os.path.join("static", "files"), exist_ok=True)
    os.makedirs("templates", exist_ok=True)

# Setup directories on startup
setup_directories()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True) 