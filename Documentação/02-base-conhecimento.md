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

[Sua descrição aqui]

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

[ex: Os JSON/CSV são carregados no início da sessão e incluídos no contexto do prompt]

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

[Sua descrição aqui]

---

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
