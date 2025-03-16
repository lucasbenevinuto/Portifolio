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
import shutil
import re
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

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

# Configuração de ambiente
TEMPLATES_DIR = "templates"
OUTPUT_DIR = "."
PAGES = [
    {"name": "home", "file": "index.html", "title": "AI & Data Science Portfolio"},
    {"name": "about", "file": "about.html", "title": "About Me"},
    {"name": "projects", "file": "projects.html", "title": "Projects"},
    {"name": "skills", "file": "skills.html", "title": "Skills & Expertise"},
    {"name": "blog", "file": "blog.html", "title": "Blog"},
    {"name": "contact", "file": "contact.html", "title": "Contact"}
]

# Configurar Jinja2
env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))

def setup_directories():
    """Garantir que todas as pastas necessárias existam."""
    os.makedirs(os.path.join("static", "css"), exist_ok=True)
    os.makedirs(os.path.join("static", "js"), exist_ok=True)
    os.makedirs(os.path.join("static", "images"), exist_ok=True)
    os.makedirs(os.path.join("static", "files"), exist_ok=True)
    os.makedirs(TEMPLATES_DIR, exist_ok=True)

def minify_css(css_content):
    """Versão simples de minificação CSS."""
    # Remover comentários
    css_content = re.sub(r'/\*.*?\*/', '', css_content, flags=re.DOTALL)
    # Remover espaços em branco desnecessários
    css_content = re.sub(r'\s+', ' ', css_content)
    css_content = re.sub(r';\s', ';', css_content)
    css_content = re.sub(r':\s', ':', css_content)
    css_content = re.sub(r',\s', ',', css_content)
    css_content = re.sub(r'{\s', '{', css_content)
    css_content = re.sub(r'\s}', '}', css_content)
    return css_content.strip()

def minify_js(js_content):
    """Versão simples de minificação JS."""
    # Remover comentários inline
    js_content = re.sub(r'//.*?\n', '\n', js_content)
    # Remover comentários multi-linha
    js_content = re.sub(r'/\*.*?\*/', '', js_content, flags=re.DOTALL)
    # Remover espaços em branco desnecessários
    js_content = re.sub(r'\s+', ' ', js_content)
    js_content = re.sub(r';\s', ';', js_content)
    js_content = re.sub(r'{\s', '{', js_content)
    js_content = re.sub(r'\s}', '}', js_content)
    js_content = re.sub(r',\s', ',', js_content)
    return js_content.strip()

def optimize_assets():
    """Otimizar CSS e JS para produção."""
    # Otimizar CSS
    css_path = os.path.join("static", "css", "styles.css")
    min_css_path = os.path.join("static", "css", "styles.min.css")
    
    if os.path.exists(css_path):
        with open(css_path, 'r', encoding='utf-8') as f:
            css_content = f.read()
        
        minified_css = minify_css(css_content)
        
        with open(min_css_path, 'w', encoding='utf-8') as f:
            f.write(minified_css)
        
        print(f"CSS otimizado: {os.path.getsize(min_css_path)} bytes")
    
    # Otimizar JS
    js_path = os.path.join("static", "js", "main.js")
    min_js_path = os.path.join("static", "js", "main.min.js")
    
    if os.path.exists(js_path):
        with open(js_path, 'r', encoding='utf-8') as f:
            js_content = f.read()
        
        minified_js = minify_js(js_content)
        
        with open(min_js_path, 'w', encoding='utf-8') as f:
            f.write(minified_js)
        
        print(f"JS otimizado: {os.path.getsize(min_js_path)} bytes")

def build_pages():
    """Construir todas as páginas HTML a partir dos templates."""
    # Verificar arquivos de template
    header_template = env.get_template('header.html')
    footer_template = env.get_template('footer.html')
    
    for page in PAGES:
        content_file = f"{page['name']}_content.html"
        
        # Skip if content template doesn't exist
        if not os.path.exists(os.path.join(TEMPLATES_DIR, content_file)):
            print(f"Aviso: Arquivo de conteúdo {content_file} não encontrado. Página {page['file']} não será gerada.")
            continue
        
        content_template = env.get_template(content_file)
        content_html = content_template.render()
        
        # Render header e footer
        header_html = header_template.render(
            page_title=page['title'],
            active_page=page['name']
        )
        footer_html = footer_template.render()
        
        # Combinar tudo em um arquivo HTML final
        output_path = os.path.join(OUTPUT_DIR, page['file'])
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(header_html)
            f.write(content_html)
            f.write(footer_html)
        
        print(f"Página gerada: {page['file']}")

def main():
    """Função principal para build do site."""
    print("Iniciando build do portfólio para GitHub Pages...")
    
    # Configuração inicial
    setup_directories()
    
    # Otimizar assets
    optimize_assets()
    
    # Gerar páginas HTML
    build_pages()
    
    print("Build concluído com sucesso!")

if __name__ == "__main__":
    main() 