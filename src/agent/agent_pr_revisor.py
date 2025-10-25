from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from pathlib import Path
import os
import ssl
import yaml

load_dotenv()

ssl._create_default_https_context = ssl._create_unverified_context

# Inicializar LLM
llm = ChatGoogleGenerativeAI(model=os.getenv("LLM_MODEL"), temperature=0.0)


def load_prompt_from_yaml(version: str = None) -> PromptTemplate:
    """
    Carrega o prompt versionado do arquivo YAML.
    
    A versão é obtida da variável de ambiente PROMPT_VERSION.
    Se não definida, usa 'v1.0.0' como padrão.
    
    Args:
        version: Versão do prompt a ser carregada. Se None, usa variável de ambiente.
        
    Returns:
        PromptTemplate configurado com o template e variáveis do YAML
        
    Raises:
        FileNotFoundError: Se o arquivo de prompt não for encontrado
    """
    # Obter versão da variável de ambiente ou usar padrão
    if version is None:
        version = os.getenv("PROMPT_VERSION", "v1.0.0")
    
    # Caminho para o arquivo de prompt
    project_root = Path(__file__).parent.parent.parent
    prompt_file = project_root / "prompts/agent-code-reviewer" / version / "prompt.yaml"
    
    # Verificar se o arquivo existe
    if not prompt_file.exists():
        raise FileNotFoundError(
            f"Arquivo de prompt não encontrado: {prompt_file}\n"
            f"Versão solicitada: {version}\n"
            f"Verifique se a variável PROMPT_VERSION está configurada corretamente."
        )
    
    # Carregar o YAML
    with open(prompt_file, 'r', encoding='utf-8') as f:
        prompt_config = yaml.safe_load(f)
    
    # Criar PromptTemplate
    prompt = PromptTemplate(
        input_variables=prompt_config['input_variables'],
        template=prompt_config['template']
    )
    
    print(f"✅ Prompt carregado com sucesso!")
    print(f"   Versão: {version}")
    print(f"   ID: {prompt_config.get('id', 'N/A')}")
    print(f"   Variáveis: {prompt_config['input_variables']}")
    
    return prompt


# Carregar o prompt versionado baseado na variável de ambiente
prompt_template = load_prompt_from_yaml()


def review_code(
    code_diff: str,
    language: str = "Python",
    repo_rules: str = "Seguir boas práticas de código limpo e PEP 8",
    security_level: str = "high",
    review_focus: str = "all"
) -> str:
    """
    Revisa código usando o prompt versionado.
    
    Args:
        code_diff: Diff do código a ser revisado
        language: Linguagem de programação
        repo_rules: Regras específicas do repositório
        security_level: Nível de segurança (high, medium, low)
        review_focus: Foco da revisão (all, security, performance, quality)
        
    Returns:
        Análise completa do código
    """
    # Formatar o prompt com as variáveis
    formatted_prompt = prompt_template.format(
        code_diff=code_diff,
        language=language,
        repo_rules=repo_rules,
        security_level=security_level,
        review_focus=review_focus
    )
    
    # Enviar para o LLM
    response = llm.invoke(formatted_prompt)
    
    return response.content