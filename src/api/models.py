"""Modelos de dados para a API."""

from pydantic import BaseModel, Field
from typing import Optional


class DiffRequest(BaseModel):
    """Modelo para requisição de revisão de diff."""
    
    diff: str = Field(..., description="Diff do código a ser revisado")
    pr_title: Optional[str] = Field(None, description="Título do PR (opcional)")
    pr_description: Optional[str] = Field(None, description="Descrição do PR (opcional)")
    language: Optional[str] = Field("Python", description="Linguagem de programação")
    repo_rules: Optional[str] = Field(
        "Seguir boas práticas de código limpo",
        description="Regras específicas do repositório"
    )
    security_level: Optional[str] = Field("high", description="Nível de segurança (high, medium, low)")
    review_focus: Optional[str] = Field("all", description="Foco da revisão (all, security, performance, quality)")
    
    class Config:
        json_schema_extra = {
            "example": {
                "diff": "diff --git a/file.py b/file.py\nindex 123..456\n--- a/file.py\n+++ b/file.py\n@@ -1,3 +1,4 @@\n def soma(a, b):\n+    # Nova funcionalidade\n     return a + b",
                "pr_title": "Adiciona comentário na função soma",
                "pr_description": "Melhora a documentação",
                "language": "Python",
                "repo_rules": "Seguir PEP 8",
                "security_level": "high",
                "review_focus": "all"
            }
        }


class RevisaoResponse(BaseModel):
    """Modelo para resposta da revisão."""
    
    status: str = Field(..., description="Status da revisão")
    message: str = Field(..., description="Mensagem de confirmação")
    diff_received: bool = Field(..., description="Se o diff foi recebido")
    diff_size: int = Field(..., description="Tamanho do diff em caracteres")
    review: Optional[str] = Field(None, description="Análise completa do código pelo agente")
    pr_title: Optional[str] = Field(None, description="Título do PR")
    language: Optional[str] = Field(None, description="Linguagem analisada")
    prompt_version: Optional[str] = Field(None, description="Versão do prompt utilizada")

