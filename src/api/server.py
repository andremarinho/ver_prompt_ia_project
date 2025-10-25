"""Servidor FastAPI para revisão de Pull Requests."""

import os
from fastapi import FastAPI, HTTPException, status
from .models import DiffRequest, RevisaoResponse
from src.agent.agent_pr_revisor import review_code


# Criação da aplicação FastAPI
app = FastAPI(
    title="PR Reviewer Agent",
    version="1.0.0",
    description="API para revisão de Pull Requests",
    docs_url="/docs",
    redoc_url="/redoc"
)


@app.get("/")
async def root():
    """Endpoint raiz."""
    prompt_version = os.getenv("PROMPT_VERSION", "v1.0.0")
    return {
        "message": "PR Reviewer Agent API",
        "version": "1.0.0",
        "prompt_version": prompt_version,
        "docs": "/docs",
        "endpoints": {
            "revisor": "/revisor",
            "health": "/health"
        }
    }


@app.get("/health")
async def health_check():
    """Verifica o status da aplicação."""
    prompt_version = os.getenv("PROMPT_VERSION", "v1.0.0")
    llm_model = os.getenv("LLM_MODEL", "gemini-pro")
    
    return {
        "status": "healthy",
        "service": "PR Reviewer Agent",
        "version": "1.0.0",
        "prompt_version": prompt_version,
        "llm_model": llm_model
    }


@app.post("/revisor", response_model=RevisaoResponse, status_code=status.HTTP_200_OK)
async def revisor(request: DiffRequest):
    """
    Endpoint para revisão de diff de Pull Request.
    
    Recebe o diff do código e retorna uma análise completa usando IA.
    
    Args:
        request: Dados do diff a ser revisado, incluindo configurações de análise
        
    Returns:
        RevisaoResponse: Análise completa do código com sugestões e recomendações
    """
    try:
        # Valida se o diff não está vazio
        if not request.diff or not request.diff.strip():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="O diff não pode estar vazio"
            )
        
        # Log da requisição
        diff_size = len(request.diff)
        print(f"\n{'='*60}")
        print(f"📝 Nova requisição de revisão")
        print(f"{'='*60}")
        print(f"   Título: {request.pr_title or 'N/A'}")
        print(f"   Linguagem: {request.language}")
        print(f"   Tamanho do diff: {diff_size} caracteres")
        print(f"   Nível de segurança: {request.security_level}")
        print(f"   Foco: {request.review_focus}")
        print(f"{'='*60}\n")
        
        # Realizar a revisão usando o agente
        print("🤖 Processando revisão com IA...")
        review_result = review_code(
            code_diff=request.diff,
            language=request.language,
            repo_rules=request.repo_rules,
            security_level=request.security_level,
            review_focus=request.review_focus
        )
        
        print("✅ Revisão concluída com sucesso!\n")
        
        # Obter versão do prompt usado
        prompt_version = os.getenv("PROMPT_VERSION", "v1.0.0")
        
        # Retorna a análise completa
        return RevisaoResponse(
            status="success",
            message="Revisão concluída com sucesso",
            diff_received=True,
            diff_size=diff_size,
            review=review_result,
            pr_title=request.pr_title,
            language=request.language,
            prompt_version=prompt_version
        )
        
    except HTTPException:
        raise
    except Exception as e:
        print(f"❌ Erro ao processar revisão: {str(e)}\n")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao processar diff: {str(e)}"
        )

