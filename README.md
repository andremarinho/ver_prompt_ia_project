# PR Reviewer Agent 🤖

API REST simples para revisão de Pull Requests usando FastAPI.

## 🚀 Instalação

### 1. Crie um ambiente virtual (na raiz do projeto)

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
# No Linux/Mac:
source venv/bin/activate

# No Windows:
venv\Scripts\activate
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Configure as variáveis de ambiente (opcional)

```bash
cp .env.example .env
```

## 🎯 Uso

### Iniciando o servidor

```bash
# A partir da raiz do projeto
python -m src.main

# Ou usando uvicorn diretamente
uvicorn src.api.server:app --reload --host 0.0.0.0 --port 8000
```

O servidor estará disponível em: `http://localhost:8000`

### Documentação da API

Acesse a documentação interativa:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 📡 Endpoint Principal

### POST /revisor

Recebe o diff de um Pull Request e retorna status 200 OK.

**Exemplo de requisição com cURL:**

```bash
curl -X POST "http://localhost:8000/revisor" \
  -H "Content-Type: application/json" \
  -d '{
    "diff": "diff --git a/file.py b/file.py\nindex 123..456\n--- a/file.py\n+++ b/file.py\n@@ -1,3 +1,4 @@\n def soma(a, b):\n+    # Nova funcionalidade\n     return a + b",
    "pr_title": "Adiciona comentário",
    "pr_description": "Melhora a documentação"
  }'
```

**Exemplo de requisição com Python:**

```python
import requests

response = requests.post(
    "http://localhost:8000/revisor",
    json={
        "diff": "diff --git a/file.py...",
        "pr_title": "Minha mudança",
        "pr_description": "Descrição das mudanças"
    }
)

print(response.status_code)  # 200
print(response.json())
```

**Resposta (200 OK):**

```json
{
  "status": "success",
  "message": "Diff recebido com sucesso",
  "diff_received": true,
  "diff_size": 150
}
```

## 🔍 Outros Endpoints

### GET /

Informações básicas da API.

### GET /health

Health check do serviço.

```bash
curl http://localhost:8000/health
```

## 📁 Estrutura do Projeto

```
ver_prompt_ia_project/           # Raiz do projeto
├── venv/                        # Ambiente virtual (não versionar)
├── src/                         # Código fonte
│   ├── __init__.py
│   ├── main.py                  # Script para iniciar servidor
│   └── api/
│       ├── __init__.py
│       ├── models.py            # Modelos Pydantic
│       └── server.py            # Servidor FastAPI
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

**Nota:** O ambiente virtual (`venv/`) deve sempre ficar na raiz do projeto, nunca dentro da pasta `src/`.

## 🛠️ Tecnologias

- **FastAPI**: Framework web moderno e rápido
- **Uvicorn**: Servidor ASGI
- **Pydantic**: Validação de dados

---

Desenvolvido com ❤️ usando FastAPI

