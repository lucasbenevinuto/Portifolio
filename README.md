# AI & Data Science Portfolio

Este é um portfólio pessoal para desenvolvedores de IA e Cientistas de Dados, otimizado para hospedagem no GitHub Pages.

## Arquitetura do Projeto

O projeto foi estruturado de forma a maximizar a performance e facilitar a manutenção:

### Estrutura de Diretórios
```
.
├── static/
│   ├── css/
│   │   ├── styles.css           # CSS original
│   │   └── styles.min.css       # CSS minificado (usado em produção)
│   ├── js/
│   │   ├── main.js              # JavaScript original
│   │   └── main.min.js          # JavaScript minificado (usado em produção)
│   ├── images/                  # Imagens otimizadas
│   └── files/                   # Arquivos para download
├── templates/
│   ├── header.html              # Template do cabeçalho
│   ├── footer.html              # Template do rodapé
│   ├── home_content.html        # Conteúdo específico da página inicial
│   ├── about_content.html       # Conteúdo específico da página sobre
│   ├── projects_content.html    # Conteúdo específico da página de projetos
│   ├── skills_content.html      # Conteúdo específico da página de habilidades
│   ├── blog_content.html        # Conteúdo específico da página de blog
│   └── contact_content.html     # Conteúdo específico da página de contato
├── index.html                   # Página inicial gerada
├── about.html                   # Página sobre gerada
├── projects.html                # Página de projetos gerada
├── skills.html                  # Página de habilidades gerada
├── blog.html                    # Página de blog gerada
├── contact.html                 # Página de contato gerada
├── 404.html                     # Página de erro 404
├── main.py                      # Script para geração do site
└── requirements.txt             # Dependências Python para geração do site
```

### Otimizações Implementadas

1. **Arquitetura Componentizada**: Cabeçalho e rodapé separados em componentes reutilizáveis.
2. **Sistema de Build**: Um script Python compila as páginas HTML a partir dos templates.
3. **Minificação de Assets**: 
   - CSS e JavaScript minificados para reduzir o tamanho dos arquivos.
   - Remoção de espaços em branco e comentários.
4. **Otimização de Carregamento**:
   - Atributo `defer` para JavaScript.
   - Atributo `rel="preconnect"` para fontes e recursos externos.
   - Número mínimo de requisições HTTP.
5. **Segurança Melhorada**:
   - Atributo `rel="noopener"` para links externos.
   - Atributos `integrity` e `crossorigin` para recursos de CDN.
6. **Acessibilidade**:
   - Uso apropriado de atributos `aria-label`.
   - Estrutura HTML semântica.

## Como Utilizar

### Requisitos
- Python 3.7 ou superior

### Instalação
```bash
pip install -r requirements.txt
```

### Gerando o Site
```bash
python main.py
```

Este comando irá:
1. Otimizar os assets (CSS e JavaScript)
2. Gerar as páginas HTML a partir dos templates
3. Preparar o site para deploy no GitHub Pages

### Customização
1. Modifique os arquivos no diretório `templates/` para alterar o conteúdo.
2. Ajuste os estilos em `static/css/styles.css`.
3. Atualize as funcionalidades em `static/js/main.js`.
4. Execute `python main.py` para reconstruir o site.

## Deploy no GitHub Pages

Para fazer o deploy do site no GitHub Pages:

1. Faça commit das mudanças no seu repositório.
2. Vá para Settings > Pages no seu repositório GitHub.
3. Selecione a branch principal (geralmente `main`) como source.
4. O site será publicado em `https://[seu-usuario].github.io/[nome-do-repositorio]/`.

## Tecnologias Utilizadas

- HTML5
- CSS3
- JavaScript
- Python (para geração do site)
- Jinja2 (para templates)
- GitHub Pages (para hospedagem)

## Licença

MIT License 