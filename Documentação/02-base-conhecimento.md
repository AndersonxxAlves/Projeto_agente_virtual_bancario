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
O agente virtual inicia seu funcionamento carregando as informações necessárias a partir dos arquivos de dados do sistema. Primeiro, ele lê os arquivos no formato JSON para obter informações estruturadas, como status de cartões e dados de empréstimos. Em seguida, ele carrega os arquivos CSV, que contêm tabelas como extratos, limites e saldos bancários.

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
BLOQUEIO DE CARTÃO (Dados/bloqueio_cartoes.json) 
{
    "cliente_id": 1001,
    "numero_conta": "58248036-1",
    "tipo_cartao": "Débito",
    "data_solicitacao_bloqueio": "2026-01-21",
    "motivo_bloqueio": "Roubo ou furto",
    "status_bloqueio": "Bloqueado",
    "canal_solicitacao": "Agência",
    "segunda_via_cartao_solicitada": true
  } 

EMPRÉSTIMO (Dados/emprestimos.json)
 {
    "cliente_id": 1001,
    "numero_conta": "58248036-1",
    "tipo_emprestimo": "Imobiliário",
    "valor_total": 32246.49,
    "taxa_juros_mensal_percentual": 2.14,
    "quantidade_parcelas": 36,
    "parcelas_pagas": 13,
    "valor_parcela": 914.9,
    "saldo_devedor": 20352.79,
    "status_emprestimo": "Em análise",
    "data_inicio": "2025-11-05",
    "proxima_parcela": "2026-12-30"
  }

  
EXTRATO BANCÁRIO (Dados/extrato_bancario.csv)

| cliente_id | numero_conta | data_movimento | tipo_movimento |  descricao   |  valor  |
|------------|--------------|----------------|----------------|--------------|---------|
|    1001    |   58248036-1 |   2026-01-15   |     Débito     |     Saque    | 958.49  |
|    1001    |   58248036-1 |   2026-01-16   |     Crédito    | TED Recebida | 2428.09 |
|    1001    |   58248036-1 |   2026-01-19   |     Crédito    |   Depósito   | 4542.53 |
|    1001    |   58248036-1 |   2026-01-20   |     Crédito    |   Depósito   | 2682.97 |
|    1001    |   58248036-1 |   2026-02-01   |     Crédito    |   Depósito   | 3444.68 |


LIMITE DE CARTÃO (Dados/limites_catoes.csv)

| cliente_id| numero_conta | limite_total | credito_utilizado | credito_disponivel | debito_diario | status_cartao |
|-----------|--------------|--------------|-------------------|--------------------|---------------|---------------|
|   1001    |  58248036-1  |   15800.56   |      7530.47      |       8270.09      |    1369.81    |   Em análise  |


SALDO BANCÁRIO (Dados/saldos_bancarios.csv)

| cliente_id | nome_cliente |    cpf     | agencia | numero_conta | tipo_conta | saldo | status_conta | data_atualizacao |
|------------|--------------|------------|---------|--------------|------------|-------|--------------|------------------|
|    1001    | João Pereira |466.273.789-65|  5316 |  58248036-1  |Conta Corrente|5727.63| Bloqueada  |    2026-02-06    |

SEGUNDA VIA DE BOLETO (Dados/segunda_via_boletos.json)
{
    "cliente_id": 1001,
    "numero_conta": "58248036-1",
    "id_boleto": "BOL532287",
    "valor_boleto": 725.95,
    "data_vencimento": "2026-01-28",
    "data_solicitacao_segunda_via": "2026-01-18",
    "motivo_solicitacao": "Atualização de vencimento",
    "status_boleto": "Pago",
    "canal_solicitacao": "App"
  }


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
