# AI & Data Science Portfolio - GitHub Pages Version

Este é um site de portfólio estático para Data Scientists e AI Engineers, otimizado para deploy no GitHub Pages.

## Visão Geral

Este portfólio foi convertido de uma aplicação FastAPI para uma versão estática compatível com GitHub Pages. O site inclui:

- Página inicial com seções para serviços, projetos em destaque e depoimentos
- Página "Sobre" com informações profissionais e educacionais
- Galeria de projetos com filtros por categoria
- Design responsivo e moderno

## Como Configurar

1. Faça um fork deste repositório
2. Ative o GitHub Pages nas configurações do repositório:
   - Vá para "Settings" > "Pages"
   - Selecione a branch "main" como source
   - Clique em "Save"

## Personalização

### Informações Pessoais

- Edite os arquivos HTML para incluir suas informações pessoais
- Atualize os links de redes sociais no rodapé de cada página
- Substitua o texto de placeholder por suas próprias informações

### Projetos

- Adicione seus próprios projetos na página `projects.html`
- Substitua as imagens em `static/images/` por imagens dos seus projetos
- Atualize os links para seus repositórios GitHub

### Imagens

- Substitua `static/images/profile.jpg` por sua foto de perfil
- Atualize as imagens de projetos em `static/images/project*.jpg`
- Personalize o favicon em `static/images/favicon.ico`

### Estilo

- O arquivo principal de estilo está em `static/css/styles.css`
- Personalize as cores, fontes e outros elementos visuais conforme necessário

## Estrutura de Arquivos

```
├── index.html              # Página inicial
├── about.html              # Página Sobre
├── projects.html           # Galeria de projetos
├── .nojekyll               # Arquivo para evitar processamento Jekyll
├── static/
│   ├── css/                # Arquivos CSS
│   ├── js/                 # Arquivos JavaScript
│   ├── images/             # Imagens
│   └── files/              # Arquivos para download (ex: currículo)
└── README.md               # Este arquivo
```

## Tecnologias Utilizadas

- HTML5
- CSS3
- JavaScript
- Font Awesome para ícones
- Google Fonts

## Licença

Este projeto está disponível como código aberto sob os termos da [Licença MIT](https://opensource.org/licenses/MIT). 