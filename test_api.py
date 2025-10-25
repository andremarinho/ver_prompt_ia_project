"""Script de teste para o endpoint de revisão."""

import requests
import json

# URL do servidor
BASE_URL = "http://localhost:8000"

# Exemplo 1: Revisão simples
print("=" * 80)
print("EXEMPLO 1: Revisão Simples de Código Python")
print("=" * 80)

example1 = {
    "diff": """diff --git a/utils.py b/utils.py
index abc123..def456 100644
--- a/utils.py
+++ b/utils.py
@@ -1,5 +1,6 @@
 def process_user_input(user_data):
-    result = eval(user_data)
+    import json
+    result = json.loads(user_data)
     return result""",
    "pr_title": "Fix security vulnerability",
    "pr_description": "Substitui eval() por json.loads() para evitar execução de código arbitrário",
    "language": "Python",
    "security_level": "high",
    "review_focus": "security"
}

response1 = requests.post(f"{BASE_URL}/revisor", json=example1)
print(f"\nStatus Code: {response1.status_code}")
if response1.status_code == 200:
    data = response1.json()
    print(f"\nMensagem: {data['message']}")
    print(f"Versão do Prompt: {data['prompt_version']}")
    print(f"Linguagem: {data['language']}")
    print(f"\n{'-' * 80}")
    print("ANÁLISE DO AGENTE:")
    print(f"{'-' * 80}")
    print(data['review'])
else:
    print(f"Erro: {response1.text}")

print("\n" + "=" * 80)
print("EXEMPLO 2: Revisão de Performance")
print("=" * 80)

example2 = {
    "diff": """diff --git a/data_processor.py b/data_processor.py
index 111222..333444 100644
--- a/data_processor.py
+++ b/data_processor.py
@@ -5,9 +5,7 @@
 def filter_items(items, condition):
-    result = []
-    for item in items:
-        if condition(item):
-            result.append(item)
-    return result
+    return [item for item in items if condition(item)]""",
    "pr_title": "Otimiza filtragem de itens",
    "pr_description": "Usa list comprehension para melhor performance",
    "language": "Python",
    "security_level": "medium",
    "review_focus": "performance"
}

response2 = requests.post(f"{BASE_URL}/revisor", json=example2)
print(f"\nStatus Code: {response2.status_code}")
if response2.status_code == 200:
    data = response2.json()
    print(f"\nMensagem: {data['message']}")
    print(f"\n{'-' * 80}")
    print("ANÁLISE DO AGENTE:")
    print(f"{'-' * 80}")
    print(data['review'][:500] + "..." if len(data['review']) > 500 else data['review'])
else:
    print(f"Erro: {response2.text}")

print("\n" + "=" * 80)
print("EXEMPLO 3: Revisão Completa (All)")
print("=" * 80)

example3 = {
    "diff": """diff --git a/auth.py b/auth.py
index aaa111..bbb222 100644
--- a/auth.py
+++ b/auth.py
@@ -10,7 +10,10 @@
 def authenticate_user(username, password):
-    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
-    return db.execute(query)
+    query = "SELECT * FROM users WHERE username=? AND password=?"
+    hashed_password = hashlib.sha256(password.encode()).hexdigest()
+    result = db.execute(query, (username, hashed_password))
+    return result""",
    "pr_title": "Corrige SQL Injection e adiciona hash de senha",
    "pr_description": "Implementa prepared statements e hash de senha",
    "language": "Python",
    "repo_rules": "Seguir OWASP Top 10, usar PEP 8, adicionar docstrings",
    "security_level": "high",
    "review_focus": "all"
}

response3 = requests.post(f"{BASE_URL}/revisor", json=example3)
print(f"\nStatus Code: {response3.status_code}")
if response3.status_code == 200:
    data = response3.json()
    print(f"\nMensagem: {data['message']}")
    print(f"Tamanho do diff: {data['diff_size']} caracteres")
    print(f"\n{'-' * 80}")
    print("ANÁLISE COMPLETA DO AGENTE:")
    print(f"{'-' * 80}")
    print(data['review'])
else:
    print(f"Erro: {response3.text}")

print("\n" + "=" * 80)
print("Testes concluídos!")
print("=" * 80)

