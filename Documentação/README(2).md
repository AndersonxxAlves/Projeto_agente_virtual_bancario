# 🏦 Íris — Agente Virtual Bancário

> Assistente virtual de atendimento bancário focado em agilidade, segurança e autonomia para o cliente.

---

## 🎯 Problema & Solução

| Dor do Cliente | Como a Íris Resolve |
|---|---|
| Filas e espera no atendimento | Respostas imediatas, 24/7 |
| Dificuldade em acessar informações da conta | Consulta direta via chat |
| Risco de fraude com cartão perdido | Bloqueio instantâneo com autenticação |
| Confusão ao simular empréstimos | Cálculo automático de parcelas |

---

## 🗂️ Etapas do Projeto

```
1. Documentação do Agente   →   2. Base de Conhecimento   →   3. Prompts
        ↓                               ↓                          ↓
  Definição de escopo,          Dados fictícios em           System prompt,
  persona e arquitetura         CSV e JSON por cliente       regras e exemplos
        ↓                               ↓                          ↓
                        4. Testes & Métricas
                   Assertividade | Segurança | Coerência
```

---

## ⚙️ Funcionalidades

| # | Serviço | Ação do Agente |
|---|---|---|
| 1 | 💰 Consultar Saldo | Exibe saldo disponível após autenticação |
| 2 | 📄 Ver Extrato | Lista movimentações por período |
| 3 | 🧮 Simular Empréstimo | Calcula parcelas, juros e total |
| 4 | 💳 Limite do Cartão | Informa total, utilizado e disponível |
| 5 | 🧾 Segunda Via de Boleto | Gera novo código de pagamento |
| 6 | 🔒 Bloquear Cartão | Bloqueio imediato por segurança |

---

## 🏗️ Arquitetura

```
Usuário
   │
   ▼
Interface (Streamlit)
   │
   ▼
LLM (Hugging Face)  ◄──►  Base de Conhecimento (CSV/JSON)
   │
   ▼
Validação de Escopo
   │
   ▼
Resposta ao Usuário
```

**Stack:** `Python` · `Streamlit` · `Hugging Face` · `Pandas` · `python-dotenv`

---

## 📁 Dados Utilizados

| Arquivo | Formato | Conteúdo |
|---|---|---|
| `saldos_bancarios_ficticios.csv` | CSV | Saldo disponível e status da conta |
| `extrato_bancario_ficticio.csv` | CSV | Histórico de movimentações |
| `limites_cartoes_ficticios.csv` | CSV | Limite total, utilizado e disponível |
| `emprestimos_ficticios.json` | JSON | Contratos, parcelas e taxas |
| `bloqueio_cartoes_ficticios.json` | JSON | Status e motivo de bloqueio |
| `segunda_via_boletos_ficticios.json` | JSON | Boletos, vencimento e código de barras |

---

## 🔐 Segurança & Limitações

**O que a Íris faz:**
- Autentica o cliente via CPF + data de nascimento
- Exibe apenas dados do titular autenticado
- Bloqueia cartão em caso de perda/roubo

**O que a Íris NÃO faz:**
- ❌ Realiza transferências ou pagamentos
- ❌ Altera dados cadastrais
- ❌ Aprova ou contrata produtos
- ❌ Desbloqueia cartões
- ❌ Fornece aconselhamento financeiro
- ❌ Responde fora do escopo bancário

---

## 📊 Métricas de Qualidade

| Métrica | O que avalia | Meta |
|---|---|---|
| **Assertividade** | Resposta correta ao que foi perguntado | ≥ 4/5 |
| **Segurança** | Evita alucinações e informações não verificadas | ≥ 4/5 |
| **Coerência** | Resposta adequada ao perfil e contexto | ≥ 4/5 |

> Testes realizados com 4 cenários: consulta de saldo, simulação de empréstimo, pergunta fora do escopo e solicitação de informação inexistente. **Todos os testes passaram.**

---

## 🚀 Como Rodar

```bash
# 1. Instalar dependências
pip install pandas streamlit python-dotenv huggingface_hub

# 2. Configurar token no arquivo .env
HUGGINGFACEHUB_API_TOKEN=seu_token_aqui

# 3. Executar
streamlit run app.py
# Acesse: http://localhost:8501
```

---

## 👤 Persona

**Nome:** Íris  
**Tom:** Profissional, cordial e objetivo  
**Linguagem:** Simples, direta, sem jargões técnicos  
**Saudação:** *"Olá! Eu sou a Íris, sua assistente virtual. Como posso te ajudar hoje?"*
