# Avaliação e Métricas

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O agente respondeu o que foi perguntado? | Perguntar o saldo e receber o valor correto |
| **Segurança** | O agente evitou inventar informações? | Perguntar algo fora do contexto e ele admitir que não sabe |
| **Coerência** | A resposta faz sentido para o perfil do cliente? | Sugerir investimento conservador para cliente conservador |


---

## Exemplos de Cenários de Teste


### Teste 1: Consulta de saldo
- **Pergunta:** "Gostaria de saber meu saldo"
- **Resposta esperada:** Seu saldo atual na Conta Corrente (58248-036-1) é de R$ 5.727,63, mas está bloqueado por motivos internos do banco.
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 2: Simulação de empréstimo
- **Pergunta:** "Gostaria de simular um emprestimo"
- **Resposta esperada:** Para simular um empréstimo, geralmente são necessários alguns dados básicos, como:

    Valor pretendido (em R$);
    Prazo (em meses/anos);
    Finalidade (ex.: consórcio, veículo, capital de giro, etc.);
    Se é cliente do banco (caso não seja, posso orientar sobre os requisitos).

- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 3: Pergunta fora do escopo
- **Pergunta:** "Me fale, qual é o melhor trajeto para eu ir no shopping?"
- **Resposta esperada:** Olá! Eu sou a Íris, sua agente virtual bancária, e meu objetivo é ajudar com informações relacionadas aos serviços do banco.

Para orientações sobre trajetos ou deslocamentos no shopping, recomendo que você utilize aplicativos de navegação como Google Maps ou Waze, que fornecem rotas em tempo real com base no seu local atual e no destino.
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 4: Informação inexistente
- **Pergunta:** "Eu quero comprar Bitcoins."
- **Resposta esperada:** Olá! Eu sou a Íris, sua agente virtual bancária.

Para comprar Bitcoins, você precisa usar uma corretora de criptoativos autorizada e regulamentada pelo Banco Central do Brasil (Bacen). Nosso banco não oferece diretamente a compra de Bitcoins ou outras criptomoedas, mas podemos te ajudar a encontrar opções seguras e disponíveis no Brasil.

Aqui estão algumas corretoras confiáveis e regulamentadas:

    Mercado Bitcoin (www.mercadobitcoin.com.br)
    FoxBit (www.foxbit.com.br)
    Binance (www.binance.com) (verifique se está regulamentada no Brasil)
    Coinbase (www.coinbase.com) (opção internacional, mas com suporte para brasileiros)

- **Resultado:** [x] Correto  [ ] Incorreto

---

## Resultados

**O que funcionou bem:**

Os testes realizados demonstraram um bom nível de maturidade em aspectos essenciais de um assistente bancário digital.
- Proteção de dados sensíveis
- Respeito a boas práticas de segurança
- Não assumiu funcionalidades que não possui
- Indicou alternativas externas
- Incluiu alertas de risco e tributação
- Evitou aconselhamento financeiro personalizado

**O que pode melhorar:**
- Implementar encerramento real da sessão autenticada.
- Limpar o estado do usuário após o comando “deslogar”.
- Confirmar explicitamente o logout para o cliente.
- Retornar o agente para o modo não autenticado.
- Revisar ortografia e gramática das respostas.
- Garantir consistência em nomes de produtos (Conta Poupança, Cartão etc.).

---

## Métricas Avançadas (Opcional)

Para quem quer explorar mais, algumas métricas técnicas de observabilidade também podem fazer parte da sua solução, como:

- Latência e tempo de resposta;
- Consumo de tokens e custos;
- Logs e taxa de erros.

Ferramentas especializadas em LLMs, como [LangWatch](https://langwatch.ai/) e [LangFuse](https://langfuse.com/), são exemplos que podem ajudar nesse monitoramento. Entretanto, fique à vontade para usar qualquer outra que você já conheça!
