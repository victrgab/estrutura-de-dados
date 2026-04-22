# 📚 Atividade: Lista Duplamente Encadeada Circular

## 📝 Descrição

Esta atividade tem como objetivo implementar operações básicas em uma **lista duplamente encadeada circular (LDDEC)** utilizando Python.

A estrutura já possui as classes base definidas (`No` e `Lddec`), e o foco é implementar corretamente os métodos solicitados.

## 🎯 Objetivo

Desenvolver as seguintes funções:

- `inserir_inicio(self, valor)`
- `inserir_fim(self, valor)`
- `remover_inicio(self)`
- `remover_fim(self)`

## ⚙️ Regras da atividade

- Implementar **somente os métodos solicitados**
- Respeitar a estrutura das classes já fornecidas
- Manter a **indentação correta**
- Atualizar corretamente o atributo `quant` após cada operação
- Não é necessário criar novos atributos na classe

## 🧠 Conceitos envolvidos

- Listas encadeadas
- Listas duplamente encadeadas
- Estruturas circulares
- Manipulação de ponteiros (referências)
- Casos especiais (lista vazia e lista com um único elemento)

## 🔄 Comportamento esperado

- A lista deve ser **circular**, ou seja:
  - O último elemento aponta para o primeiro
  - O primeiro elemento aponta para o último

- Cada nó deve conter:
  - Referência para o nó anterior
  - Valor armazenado
  - Referência para o próximo nó

## ⚠️ Pontos de atenção

- Tratar corretamente:
  - Lista vazia
  - Lista com apenas um elemento
- Garantir que os ponteiros (`ant` e `prox`) estejam sempre consistentes
- Não esquecer de atualizar o tamanho da lista (`quant`)

## 📌 Observação

Esta atividade é focada no entendimento da estrutura de dados e na manipulação correta dos nós, não sendo necessário implementar funcionalidades extras além das solicitadas.

---

## 👤 Autor

Victor