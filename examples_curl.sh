"""Exemplo de uso da API com cURL."""

# EXEMPLO 1: Revisão Simples
curl -X POST "http://localhost:8000/revisor" \
  -H "Content-Type: application/json" \
  -d '{
    "diff": "diff --git a/utils.py b/utils.py\nindex abc123..def456 100644\n--- a/utils.py\n+++ b/utils.py\n@@ -1,5 +1,6 @@\n def process_user_input(user_data):\n-    result = eval(user_data)\n+    import json\n+    result = json.loads(user_data)\n     return result",
    "pr_title": "Fix security vulnerability",
    "language": "Python",
    "security_level": "high",
    "review_focus": "security"
  }'

# EXEMPLO 2: Revisão com todas as opções
curl -X POST "http://localhost:8000/revisor" \
  -H "Content-Type: application/json" \
  -d '{
    "diff": "diff --git a/auth.py b/auth.py\n+++ melhorias de segurança",
    "pr_title": "Melhora autenticação",
    "pr_description": "Adiciona validação e hash",
    "language": "Python",
    "repo_rules": "Seguir PEP 8 e OWASP Top 10",
    "security_level": "high",
    "review_focus": "all"
  }'

# EXEMPLO 3: Health Check
curl http://localhost:8000/health

# EXEMPLO 4: Info da API
curl http://localhost:8000/

