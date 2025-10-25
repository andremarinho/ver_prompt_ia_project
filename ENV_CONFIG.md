# Configuração de Variáveis de Ambiente

## Variáveis Necessárias

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```env
# Configuração do servidor
API_HOST=0.0.0.0
API_PORT=8000
DEBUG=True

# Configuração do LLM (Google Gemini)
LLM_MODEL=gemini-pro
GOOGLE_API_KEY=your-google-api-key-here

# Versão do Prompt a ser utilizado
PROMPT_VERSION=v1.0.0

# Configurações SSL (se necessário)
# GRPC_DEFAULT_SSL_ROOTS_FILE_PATH=/path/to/certs/nscacert.pem
```

## Descrição das Variáveis

### Servidor
- **API_HOST**: Host onde o servidor será executado (padrão: 0.0.0.0)
- **API_PORT**: Porta do servidor (padrão: 8000)
- **DEBUG**: Modo debug (True/False)

### LLM
- **LLM_MODEL**: Modelo do Google Gemini a ser usado (gemini-pro, gemini-1.5-pro, etc.)
- **GOOGLE_API_KEY**: Chave de API do Google AI Studio

### Prompts
- **PROMPT_VERSION**: Versão do prompt a ser carregada (padrão: v1.0.0)
  - Define qual versão do prompt em `prompts/{version}/prompt.yaml` será usada
  - Permite trocar de versão sem alterar código
  - Exemplos: v1.0.0, v1.1.0, v2.0.0

### SSL (Opcional)
- **GRPC_DEFAULT_SSL_ROOTS_FILE_PATH**: Caminho para certificados SSL customizados

## Como Obter as Chaves

### Google API Key
1. Acesse [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Crie uma nova API Key
3. Copie e cole no arquivo `.env`

## Exemplo de Uso

```bash
# Criar arquivo .env
cp .env.example .env

# Editar com suas configurações
nano .env

# Instalar dependências
pip install -r requirements.txt

# Executar servidor
python -m src.main
```

## Trocar Versão do Prompt

Para usar uma versão diferente do prompt:

```env
# No arquivo .env
PROMPT_VERSION=v1.1.0
```

Ou definir no terminal:

```bash
export PROMPT_VERSION=v1.1.0
python -m src.main
```

## Validação

O sistema validará automaticamente:
- Se a versão do prompt existe
- Se todas as variáveis necessárias estão definidas
- Se os arquivos de prompt estão acessíveis

Mensagens de erro claras serão exibidas caso algo esteja incorreto.

