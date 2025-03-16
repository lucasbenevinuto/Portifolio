# FastAPI Básico

Estrutura básica para uma aplicação FastAPI.

## Instalação

1. Clone o repositório
2. Crie um ambiente virtual e ative-o:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure o arquivo .env com suas variáveis de ambiente

## Executando o projeto

```bash
python main.py
```

A aplicação estará disponível em http://localhost:8000

A documentação da API estará disponível em:
- http://localhost:8000/docs (Swagger UI)
- http://localhost:8000/redoc (ReDoc)

## Estrutura do projeto

```
├── app/
│   ├── routers/
│   │   ├── items.py
│   │   └── users.py
│   ├── schemas/
│   │   ├── item.py
│   │   └── user.py
├── .env
├── main.py
├── requirements.txt
└── README.md
``` 