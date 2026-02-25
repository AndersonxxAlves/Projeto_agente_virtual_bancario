import pandas as pd
import streamlit as st
import json
from pathlib import Path
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
import os

# ================= CONFIG =================

load_dotenv()

hf_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

client = InferenceClient(
    model="mistralai/Mistral-7B-Instruct-v0.2",
    token=hf_token
)

# ================= BANCO DE DADOS =================

class BancoDados:
    def __init__(self, pasta_dados=None):

        base_dir = Path(__file__).resolve().parent

        if pasta_dados:
            self.pasta = Path(pasta_dados).resolve()
        else:
            self.pasta = base_dir
            if (base_dir / "data").exists():
                self.pasta = base_dir / "data"

        print(f"Carregando arquivos de: {self.pasta}")
        self._carregar_dados()

    def _carregar_dados(self):

        def carregar_csv(nome):
            caminho = self.pasta / nome
            if caminho.exists():
                return pd.read_csv(caminho)
            return pd.DataFrame()

        def carregar_json(nome):
            caminho = self.pasta / nome
            if caminho.exists():
                with open(caminho, encoding="utf-8") as f:
                    return pd.DataFrame(json.load(f))
            return pd.DataFrame()

        self.saldos = carregar_csv("saldos_bancarios_ficticios.csv")
        self.extrato = carregar_csv("extrato_bancario_ficticio.csv")
        self.limites = carregar_csv("limites_cartoes_ficticios.csv")
        self.emprestimos = carregar_json("emprestimos_ficticios.json")
        self.bloqueios = carregar_json("bloqueio_cartoes_ficticios.json")
        self.boletos = carregar_json("segunda_via_boletos_ficticios.json")

    # ========= CONSULTAS ============
    def _filtrar(self, df, cliente_id):
        if df.empty or "cliente_id" not in df.columns:
            return pd.DataFrame()
        return df[df["cliente_id"] == cliente_id]

    def obter_saldo(self, cliente_id):
        return self._filtrar(self.saldos, cliente_id)

    def obter_extrato(self, cliente_id):
        return self._filtrar(self.extrato, cliente_id)

    def obter_limites_cartao(self, cliente_id):
        return self._filtrar(self.limites, cliente_id)

    def obter_emprestimos(self, cliente_id):
        return self._filtrar(self.emprestimos, cliente_id)

    def obter_bloqueios_cartao(self, cliente_id):
        return self._filtrar(self.bloqueios, cliente_id)

    def obter_boletos(self, cliente_id):
        return self._filtrar(self.boletos, cliente_id)


# ================= ASSISTENTE =================

class AssistenteBancario:
    def __init__(self, banco_dados):
        self.db = banco_dados

    def gerar_contexto_cliente(self, cliente_id):
        saldo = self.db.obter_saldo(cliente_id)
        limite = self.db.obter_limites_cartao(cliente_id)
        bloqueio = self.db.obter_bloqueios_cartao(cliente_id)

        return f"""
Cliente ID: {cliente_id}

SALDO:
{saldo.to_dict(orient="records")}

LIMITE CARTÃO:
{limite.to_dict(orient="records")}

BLOQUEIO:
{bloqueio.to_dict(orient="records")}
"""


# ================= SYSTEM PROMPT =================

SYSTEM_PROMPT = """
Íris é uma agente virtual de assistência bancária criada para tornar a experiência financeira dos clientes mais simples, rápida e segura. Com uma comunicação clara, amigável e objetiva, ela entende as necessidades do usuário e oferece suporte imediato no dia a dia, ajudando a acompanhar informações importantes da conta e a resolver demandas comuns sem complicação.

Objetivo:
A Íris tem como objetivo principal oferecer ao cliente uma experiência bancária ágil, segura e autônoma para o acompanhamento e a gestão de suas principais demandas financeiras do dia a dia. Sua proposta é centralizar, em um único canal de atendimento, as interações mais recorrentes relacionadas à consulta de saldo, visualização de extrato, simulação de empréstimo, verificação de limite do cartão, emissão de segunda via de boletos e bloqueio de cartão.

REGRAS:
1 - Não realizar transações financeiras
Íris não deve efetuar transferências, pagamentos, investimentos ou qualquer movimentação de valores.

2 - Não alterar dados cadastrais do cliente
A agente não pode modificar informações pessoais, como endereço, telefone, e-mail ou dados bancários.

3 - Não fornecer aconselhamento financeiro personalizado
Íris não deve recomendar produtos financeiros, investimentos ou decisões de crédito com caráter consultivo.

4 - Não aprovar ou contratar produtos
A agente não tem permissão para efetivar contratação de empréstimos, cartões ou quaisquer serviços — apenas apresentar simulações informativas.

5 - Não compartilhar informações sem autenticação válida
Íris não deve exibir dados sensíveis caso a verificação de identidade do cliente não esteja concluída com sucesso.

6 - Não executar desbloqueio de cartão
A agente pode permitir o bloqueio por segurança, mas não deve realizar o desbloqueio do cartão.

7 - Não acessar ou expor dados de terceiros
Íris deve limitar as informações exclusivamente ao titular autenticado, sem qualquer exceção.

8 - Não sair do escopo funcional definido
A agente não deve responder ou executar solicitações fora de suas atribuições principais.

9 - Não armazenar informações sensíveis em conversas
Íris não deve solicitar nem reter senhas completas, códigos de segurança ou dados confidenciais desnecessários.

10 - Não fornecer garantias ou promessas
A agente não deve assegurar aprovação de crédito, prazos bancários ou resultados que dependam de análise sistêmica.

"""

# ================= FUNÇÃO PERGUNTAR =================

def perguntar(msg, contexto_cliente):

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": f"""
CONTEXTO DO CLIENTE:
{contexto_cliente}

PERGUNTA:
{msg}

Responda em português.
"""
        }
    ]

    response = client.chat_completion(
        messages=messages,
        max_tokens=500,
        temperature=0.3
    )

    return response.choices[0].message.content


# ================= STREAMLIT =================

st.set_page_config(page_title="Assistente Íris")
st.title("Olá! Eu sou a Íris, em que posso ajudar?")


if "autenticado" not in st.session_state:
    st.session_state.autenticado = False

if "cliente_id" not in st.session_state:
    st.session_state.cliente_id = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

banco = BancoDados()
assistente = AssistenteBancario(banco)

# ================= ENTRADA / PERGUNTA OU SOLICITAÇÃO =================

mensagem = st.chat_input("Digite sua mensagem...")

if mensagem:

    st.session_state.chat_history.append(("user", mensagem))

    # ================= VERIFICA SE PRECISA LOGIN =================
    palavras_sensiveis = ["saldo", "extrato", "limite", "cartão", "boleto", "empréstimo"]

    precisa_login = any(p in mensagem.lower() for p in palavras_sensiveis)

    if precisa_login and not st.session_state.autenticado:

        st.session_state.chat_history.append(
            ("assistant", "Para acessar essas informações, preciso que você informe seu ID de cliente para autenticação.")
        )

    elif not st.session_state.autenticado and mensagem.isdigit():

        cliente_id = int(mensagem)
        st.session_state.cliente_id = cliente_id
        st.session_state.autenticado = True

        st.session_state.chat_history.append(
            ("assistant", "Autenticação realizada com sucesso! Como posso ajudar agora?")
        )

    else:

        contexto = ""

        if st.session_state.autenticado:
            contexto = assistente.gerar_contexto_cliente(
                st.session_state.cliente_id
            )

        resposta = perguntar(mensagem, contexto)

        st.session_state.chat_history.append(("assistant", resposta))


# ================= EXIBIR RESPOSTA =================

for role, content in st.session_state.chat_history:
    with st.chat_message(role):
        st.write(content)
