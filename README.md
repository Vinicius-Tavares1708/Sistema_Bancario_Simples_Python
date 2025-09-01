# Sistema Bancário Simples

Este é um projeto de console em Python que simula um sistema bancário simples, permitindo que o usuário realize operações básicas como depósito, saque e verificação de extrato. O programa opera com um saldo inicial e aplica regras de negócio para as transações.

---

### Funcionalidades

O sistema oferece um menu interativo com as seguintes opções:

* **Depósito:** Adiciona um valor ao saldo da conta, com validação para garantir que o valor seja positivo.
* **Saque:** Permite sacar um valor, respeitando o limite por transação (R$ 500) e o limite de 3 saques diários.
* **Extrato:** Exibe o histórico de todas as transações (depósitos e saques) e o saldo atual da conta.
* **Sair:** Encerra o programa.

---

### Conceitos de Programação Utilizados

Este projeto foi desenvolvido para praticar e demonstrar o uso de conceitos fundamentais em Python:

* **Estruturas de Repetição:** Uso de um laço `while` para manter o menu do programa em execução contínua.
* **Condicionais:** Utilização de `if`, `elif` e `else` para controlar o fluxo do programa, validar entradas e aplicar as regras de negócio.
* **Listas:** Armazenamento do histórico de transações em uma lista, que serve como um extrato.
* **Variáveis e Constantes:** Gerenciamento do saldo, contagem de saques e definição de limites de saque usando variáveis e uma constante (`LIMITE_SAQUE`).
* **Formatação de Strings:** Uso de f-strings para exibir valores monetários de forma formatada (`R$XX.XX`).
* **Entrada e Saída de Dados:** Interação com o usuário através de `input()` e `print()`.
