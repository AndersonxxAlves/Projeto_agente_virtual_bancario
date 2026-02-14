# Base de Conhecimento

## Dados Utilizados

| Arquivo | Formato | Estrutura de trabalho do agente |
|---------|---------|---------------------|
| `bloqueio_cartoes.json` | JSON | Após a autenticação do cliente, o sistema realiza o bloqueio do cartão solicitado, impedindo novas transações por segurança. Em seguida, são exibidas informações como status do cartão, motivo do bloqueio e orientações para os próximos passos, como solicitação de segunda via ou possibilidade de desbloqueio. Essa ação ajuda a proteger o cliente contra usos indevidos e possíveis prejuízos financeiros. |
| `emprestimos.json` | JSON | Após a autenticação do cliente, o sistema apresenta as opções de empréstimo disponíveis de acordo com o perfil analisado. Em seguida, são exibidas informações como valor máximo liberado, taxas de juros, prazo para pagamento e valor estimado das parcelas. Essa visualização ajuda o cliente a avaliar as condições e planejar a contratação de forma consciente. |
| `extrato_bancario.csv` | CSV | Após a autenticação do cliente, o sistema gera e exibe o extrato bancário referente ao período solicitado. Em seguida, são apresentadas informações como saldo inicial, entradas, saídas, tarifas e saldo final da conta. Essa visualização ajuda o cliente a acompanhar suas movimentações e manter um melhor controle financeiro. |
| `limites_cartoes.csv` | CSV | Após a autenticação do cliente, o sistema exibe informações como limite total, limite disponível, valor já utilizado e, no caso do débito, o saldo da conta vinculada. Essa verificação ajuda o cliente a planejar melhor seus gastos e evitar recusas em transações. |
| `segunda_via_boletos.json` | JSON | Após a autenticação do cliente, o sistema localiza e disponibiliza a segunda via do boleto solicitado. Em seguida, são exibidas informações como valor atualizado, data de vencimento, código de barras ou linha digitável e status do pagamento. Essa visualização permite que o cliente realize o pagamento corretamente e evite encargos por atraso. |
| `saldos_bancarios.csv` | CSV | Após a autenticação do cliente, o sistema consulta e exibe os saldos das contas vinculadas. Em seguida, são apresentadas informações como saldo disponível, saldo bloqueado (se houver) e limite do cheque especial. Essa visualização ajuda o cliente a acompanhar sua posição financeira e planejar melhor suas movimentações. |
> [!TIP]


---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Houve uma mudança importante no foco e na finalidade dos dados utilizados pelo agente. Antes, a estrutura era mais voltada para análise de perfil financeiro e apoio a decisões de investimento, indicando um agente com atuação mais consultiva e estratégica. Com a atualização, o conjunto de dados passou a priorizar informações operacionais do dia a dia bancário, direcionando o agente para um papel mais prático de atendimento ao cliente.

---

## Estratégia de Integração

### Como os dados são carregados?
> O agente virtual inicia seu funcionamento carregando as informações necessárias a partir dos arquivos de dados do sistema. Primeiro, ele lê os arquivos no formato JSON para obter informações estruturadas, como status de cartões e dados de empréstimos. Em seguida, ele carrega os arquivos CSV, que contêm tabelas como extratos, limites e saldos bancários.

```import json
import pandas as pd

# --- Carregamento dos arquivos JSON ---

with open("bloqueio_cartoes.json", "r", encoding="utf-8") as f:
    bloqueio_cartoes = json.load(f)

with open("emprestimos.json", "r", encoding="utf-8") as f:
    emprestimos = json.load(f)

# --- Carregamento dos arquivos CSV ---

extrato_bancario = pd.read_csv("extrato_bancario.csv")
limites_cartoes = pd.read_csv("limites_cartoes.csv")
saldos_bancarios = pd.read_csv("saldos_bancarios.csv")

# --- Exemplo de uso pelo agente virtual ---

print("Dados carregados com sucesso!\n")

print("Bloqueio de cartões:")
print(bloqueio_cartoes)

print("\nEmpréstimos:")
print(emprestimos)

print("\nExtrato bancário (primeiras linhas):")
print(extrato_bancario.head())

print("\nLimites de cartões (primeiras linhas):")
print(limites_cartoes.head())

print("\nSaldos bancários (primeiras linhas):")
print(saldos_bancarios.head())
``` 

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

```text
Bloqueio de cartão
[
  {
    "cliente_id": 1001,
    "numero_conta": "58248036-1",
    "tipo_cartao": "Débito",
    "data_solicitacao_bloqueio": "2026-01-21",
    "motivo_bloqueio": "Roubo ou furto",
    "status_bloqueio": "Bloqueado",
    "canal_solicitacao": "Agência",
    "segunda_via_cartao_solicitada": true
  },
  {
    "cliente_id": 1004,
    "numero_conta": "47083312-1",
    "tipo_cartao": "Débito",
    "data_solicitacao_bloqueio": "2026-01-17",
    "motivo_bloqueio": "Roubo ou furto",
    "status_bloqueio": "Solicitado",
    "canal_solicitacao": "Central Telefônica",
    "segunda_via_cartao_solicitada": true
  },
  {
    "cliente_id": 1005,
    "numero_conta": "16148459-5",
    "tipo_cartao": "Crédito",
    "data_solicitacao_bloqueio": "2026-01-18",
    "motivo_bloqueio": "Suspeita de fraude",
    "status_bloqueio": "Em processamento",
    "canal_solicitacao": "Central Telefônica",
    "segunda_via_cartao_solicitada": true
  },
  {
    "cliente_id": 1006,
    "numero_conta": "99447152-9",
    "tipo_cartao": "Múltiplo",
    "data_solicitacao_bloqueio": "2026-01-16",
    "motivo_bloqueio": "Solicitação do cliente",
    "status_bloqueio": "Bloqueado",
    "canal_solicitacao": "App",
    "segunda_via_cartao_solicitada": false
  },
  {
    "cliente_id": 1011,
    "numero_conta": "77434354-9",
    "tipo_cartao": "Crédito",
    "data_solicitacao_bloqueio": "2026-01-25",
    "motivo_bloqueio": "Solicitação do cliente",
    "status_bloqueio": "Bloqueado",
    "canal_solicitacao": "Internet Banking",
    "segunda_via_cartao_solicitada": false
  },
  {
    "cliente_id": 1014,
    "numero_conta": "72549446-5",
    "tipo_cartao": "Crédito",
    "data_solicitacao_bloqueio": "2026-01-14",
    "motivo_bloqueio": "Roubo ou furto",
    "status_bloqueio": "Reemitido",
    "canal_solicitacao": "Agência",
    "segunda_via_cartao_solicitada": false
  },
  {
    "cliente_id": 1015,
    "numero_conta": "33493673-7",
    "tipo_cartao": "Múltiplo",
    "data_solicitacao_bloqueio": "2026-01-24",
    "motivo_bloqueio": "Solicitação do cliente",
    "status_bloqueio": "Solicitado",
    "canal_solicitacao": "Agência",
    "segunda_via_cartao_solicitada": true
  },
  {
    "cliente_id": 1017,
    "numero_conta": "29416882-3",
    "tipo_cartao": "Crédito",
    "data_solicitacao_bloqueio": "2026-01-20",
    "motivo_bloqueio": "Solicitação do cliente",
    "status_bloqueio": "Reemitido",
    "canal_solicitacao": "Internet Banking",
    "segunda_via_cartao_solicitada": false
  },
  {
    "cliente_id": 1019,
    "numero_conta": "35850594-5",
    "tipo_cartao": "Débito",
    "data_solicitacao_bloqueio": "2026-02-04",
    "motivo_bloqueio": "Perda do cartão",
    "status_bloqueio": "Reemitido",
    "canal_solicitacao": "Central Telefônica",
    "segunda_via_cartao_solicitada": false
  },
  {
    "cliente_id": 1022,
    "numero_conta": "62899666-1",
    "tipo_cartao": "Débito",
    "data_solicitacao_bloqueio": "2026-02-01",
    "motivo_bloqueio": "Roubo ou furto",
    "status_bloqueio": "Solicitado",
    "canal_solicitacao": "App",
    "segunda_via_cartao_solicitada": true
  },
  {
    "cliente_id": 1025,
    "numero_conta": "40685201-9",
    "tipo_cartao": "Crédito",
    "data_solicitacao_bloqueio": "2026-02-10",
    "motivo_bloqueio": "Suspeita de fraude",
    "status_bloqueio": "Solicitado",
    "canal_solicitacao": "App",
    "segunda_via_cartao_solicitada": true
  },
  {
    "cliente_id": 1027,
    "numero_conta": "65662246-1",
    "tipo_cartao": "Crédito",
    "data_solicitacao_bloqueio": "2026-01-29",
    "motivo_bloqueio": "Solicitação do cliente",
    "status_bloqueio": "Em processamento",
    "canal_solicitacao": "Central Telefônica",
    "segunda_via_cartao_solicitada": true
  },
  {
    "cliente_id": 1028,
    "numero_conta": "69706377-9",
    "tipo_cartao": "Crédito",
    "data_solicitacao_bloqueio": "2026-01-18",
    "motivo_bloqueio": "Suspeita de fraude",
    "status_bloqueio": "Em processamento",
    "canal_solicitacao": "Agência",
    "segunda_via_cartao_solicitada": true
  },
  {
    "cliente_id": 1030,
    "numero_conta": "49753080-9",
    "tipo_cartao": "Débito",
    "data_solicitacao_bloqueio": "2026-01-29",
    "motivo_bloqueio": "Roubo ou furto",
    "status_bloqueio": "Bloqueado",
    "canal_solicitacao": "Central Telefônica",
    "segunda_via_cartao_solicitada": false
  }
]

Empréstimo

Extrato bancário

Limite do cartão

Saldo bancário

Segunda via de boleto



---
```

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
Dados do Cliente:
- Nome: João Silva
- Perfil: Moderado
- Saldo disponível: R$ 5.000

Últimas transações:
- 01/11: Supermercado - R$ 450
- 03/11: Streaming - R$ 55
...
```
