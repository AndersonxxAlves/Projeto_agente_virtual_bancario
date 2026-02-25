# Etapas da execução


## 1. Instalar as bibliotecas

No terminal do VS Code:

pip install pandas streamlit python-dotenv huggingface_hub
🔹 Bibliotecas principais

pandas → leitura de CSV/JSON

streamlit → interface web do chat

python-dotenv → leitura do token no .env

huggingface_hub → conexão com o modelo de IA

## 2. Configurar o token da Hugging Face

Crie um arquivo .env na raiz:

HUGGINGFACEHUB_API_TOKEN=seu_token_aqui

O código usa:

load_dotenv()
hf_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

Isso autentica o acesso ao modelo.

## 3. Entender as partes principais do código
Classe BancoDados

Responsável por:

carregar CSV/JSON

filtrar por cliente_id

fornecer dados do cliente

Métodos principais:

obter_saldo

obter_extrato

obter_limites_cartao

obter_emprestimos

🤖 Classe AssistenteBancario

Função principal:

gerar_contexto_cliente(cliente_id)

👉 Monta o contexto do cliente para enviar ao LLM.

🧠 Função perguntar

Responsável por:

montar o prompt

enviar ao modelo

retornar a resposta

É o coração da IA.

💬 Streamlit

Controla:

interface do chat

autenticação simples

histórico da conversa

## 4. Executar o projeto

No terminal:

streamlit run nome_do_arquivo.py

Exemplo:

streamlit run app.py

Depois abra no navegador:

http://localhost:8501
## 5. Fluxo de funcionamento

O sistema funciona assim:

Usuário envia mensagem

Sistema verifica se precisa login

Se autenticado → gera contexto

Envia pergunta ao modelo

Íris responde no chat
