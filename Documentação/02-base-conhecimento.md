# Base de Conhecimento

## Dados Utilizados

| Arquivo | Formato | Estrutura de trabalho do agente |
|---------|---------|---------------------|
| `bloqueio_cartoes.json` | JSON | Após a autenticação do cliente, o sistema realiza o bloqueio do cartão solicitado, impedindo novas transações por segurança. Em seguida, são exibidas informações como status do cartão, motivo do bloqueio e orientações para os próximos passos, como solicitação de segunda via ou possibilidade de desbloqueio. Essa ação ajuda a proteger o cliente contra usos indevidos e possíveis prejuízos financeiros. |
| `emprestimos.json` | JSON | O cliente acessa o agente e solicita uma simulação de empréstimo. |
| `extrato_bancario.csv` | CSV | Através do agente o cliente pode consultar o extrato da sua conta |
| `limites_cartoes.csv` | CSV | Após a autenticação do cliente, o sistema exibe informações como limite total, limite disponível, valor já utilizado e, no caso do débito, o saldo da conta vinculada. Essa verificação ajuda o cliente a planejar melhor seus gastos e evitar recusas em transações. |
| `segunda_via_boletos.json` | JSON |
| `saldos_bancarios.csv` | CSV |
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
