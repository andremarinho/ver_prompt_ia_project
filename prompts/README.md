# 📝 Prompts Versionados

Este diretório contém os prompts versionados do Agent Code Reviewer.

## 🎯 Sobre

Os prompts são versionados para garantir:
- ✅ Rastreabilidade de mudanças
- ✅ Rollback para versões anteriores
- ✅ Testes A/B de diferentes abordagens
- ✅ Documentação evolutiva
- ✅ Reprodutibilidade das análises

## 📁 Estrutura

```
prompts/
├── README.md           # Este arquivo
├── v1.0.0/            # Versão 1.0.0
│   └── prompt.yaml    # Prompt do agente revisor
├── v1.1.0/            # Versão 1.1.0 (futura)
│   └── prompt.yaml
└── ...
```

## 📋 Versões Disponíveis

### v1.0.0 (Atual)

**ID:** `agent-code-reviewer`  
**Status:** ✅ Ativo  
**Data:** 2024

**Descrição:**
Prompt inicial do Agent Code Reviewer com análise completa de código focada em 5 aspectos principais: Segurança, Performance, Qualidade do Código, Boas Práticas e Manutenibilidade.

**Variáveis de entrada:**
- `code_diff` - Diff do código a ser revisado
- `language` - Linguagem de programação
- `repo_rules` - Regras específicas do repositório
- `security_level` - Nível de rigor de segurança
- `review_focus` - Foco principal da revisão

**Aspectos analisados:**
1. **Segurança** - Vulnerabilidades OWASP Top 10, validação, sanitização
2. **Performance** - Complexidade algorítmica, otimizações, gargalos
3. **Qualidade** - Legibilidade, padrões, nomenclatura, estrutura
4. **Boas Práticas** - SOLID, design patterns, tratamento de erros
5. **Manutenibilidade** - Acoplamento, duplicação, escalabilidade

**Formato de saída:**
- Resumo Executivo
- Issues Críticos (`[CRITICAL]`)
- Melhorias Recomendadas (`[PERFORMANCE]`, `[SECURITY]`, `[QUALITY]`, `[MAINTAINABILITY]`)
- Pontos Positivos
- Próximos Passos

## 🔧 Como Usar

### Formato YAML

Os prompts seguem o formato:

```yaml
_type: prompt
id: agent-code-reviewer
version: 1.0.0
input_variables:
  - variavel1
  - variavel2
template: |
  Template do prompt com {variavel1} e {variavel2}
```

### Carregando um Prompt

```python
import yaml

# Carregar prompt específico
with open('prompts/v1.0.0/prompt.yaml', 'r') as f:
    prompt_config = yaml.safe_load(f)

# Acessar template
template = prompt_config['template']
variables = prompt_config['input_variables']

# Usar o template
prompt_filled = template.format(
    code_diff="...",
    language="Python",
    repo_rules="...",
    security_level="high",
    review_focus="all"
)
```

### Integrando com LangChain

```python
from langchain.prompts import PromptTemplate
import yaml

# Carregar configuração
with open('prompts/v1.0.0/prompt.yaml', 'r') as f:
    config = yaml.safe_load(f)

# Criar PromptTemplate
prompt = PromptTemplate(
    input_variables=config['input_variables'],
    template=config['template']
)

# Usar
formatted_prompt = prompt.format(
    code_diff="diff --git...",
    language="Python",
    repo_rules="Use PEP 8",
    security_level="high",
    review_focus="security"
)
```

## 📊 Versionamento Semântico

Seguimos o padrão **Semantic Versioning** (MAJOR.MINOR.PATCH):

- **MAJOR** (v2.0.0): Mudanças incompatíveis na estrutura ou variáveis
- **MINOR** (v1.1.0): Adição de funcionalidades mantendo compatibilidade
- **PATCH** (v1.0.1): Correções e melhorias menores

### Exemplos de mudanças:

**MAJOR (v2.0.0)**:
- Remover ou renomear variáveis de entrada
- Mudar completamente a estrutura da resposta
- Alterar fundamentalmente a abordagem de análise

**MINOR (v1.1.0)**:
- Adicionar novas variáveis de entrada (opcionais)
- Expandir seções de análise
- Melhorar detalhamento das respostas

**PATCH (v1.0.1)**:
- Corrigir typos
- Melhorar clareza de instruções
- Ajustar pequenos detalhes do formato

## 🚀 Criando uma Nova Versão

1. **Criar diretório da versão:**
```bash
mkdir prompts/v1.1.0
```

2. **Copiar versão anterior:**
```bash
cp prompts/v1.0.0/prompt.yaml prompts/v1.1.0/prompt.yaml
```

3. **Editar o arquivo:**
```yaml
_type: prompt
id: agent-code-reviewer
version: 1.1.0  # Atualizar versão
input_variables:
  - code_diff
  - language
  # ... suas modificações
template: |
  # ... suas modificações
```

4. **Atualizar este README** com informações da nova versão

5. **Commit com mensagem clara:**
```bash
git add prompts/v1.1.0/
git commit -m "feat(prompts): adiciona v1.1.0 com análise de testes"
```

## 📝 Boas Práticas

### ✅ Faça

- Versione toda mudança significativa no prompt
- Documente as mudanças neste README
- Mantenha compatibilidade backward quando possível
- Teste a nova versão antes de marcar como ativa
- Use mensagens de commit descritivas

### ❌ Não Faça

- Editar prompts de versões anteriores (crie nova versão)
- Deletar versões antigas (manter histórico)
- Fazer múltiplas mudanças não relacionadas na mesma versão
- Usar caracteres especiais nos nomes de variáveis

## 🔍 Changelog

### v1.0.0 (2024)
- ✨ Versão inicial do Agent Code Reviewer
- ✨ Análise completa em 5 dimensões
- ✨ Suporte a múltiplas linguagens
- ✨ Formato de resposta estruturado
- ✨ Variáveis contextuais (language, security_level, review_focus)

## 📚 Referências

- [Semantic Versioning](https://semver.org/)
- [LangChain Prompts](https://python.langchain.com/docs/modules/model_io/prompts/)
- [YAML Specification](https://yaml.org/spec/)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)

## 🤝 Contribuindo

Para sugerir melhorias nos prompts:

1. Abra uma issue descrevendo a melhoria
2. Proponha a nova versão com exemplo
3. Documente o impacto e benefícios
4. Aguarde revisão e feedback

---

**Mantido por:** Equipe de Desenvolvimento  
**Última atualização:** 2025

