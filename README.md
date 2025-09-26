# 🏦 Sistema Bancário Simples em Python (POO)

Este projeto é uma implementação de um sistema bancário simples, focado na aplicação e demonstração de conceitos avançados de **Programação Orientada a Objetos (POO)** em Python.

O sistema permite o cadastro de clientes e contas, a realização de transações (depósito e saque) e a visualização do histórico, tudo gerenciado por classes bem definidas.

---

## 💡 Conceitos de POO Aplicados

O coração deste projeto é a estruturação em classes que se comunicam, utilizando os pilares da POO:

| Conceito | Aplicação no Código |
| :--- | :--- |
| **Abstração** | A classe `Transacao(ABC)` define um contrato. Classes filhas (`Saque`, `Deposito`) são obrigadas a implementar métodos como `registrar()`, garantindo o fluxo da aplicação. |
| **Herança** | `PessoaFisica` herda de `Cliente`, e `ContaCorrente` herda de `Conta`, reaproveitando atributos e métodos e adicionando lógicas específicas. |
| **Encapsulamento** | Uso de atributos privados (`_saldo`, `_agencia`) e do decorador **`@property`** para controlar o acesso e a manipulação dos dados internos das contas. |
| **Polimorfismo** | O método `sacar()` se comporta de maneira diferente na classe base (`Conta`) e na classe filha (`ContaCorrente`), que adiciona validações de limite e de quantidade de saques. |

---

## ✨ Funcionalidades

O sistema é operado via menu de console e oferece as seguintes opções:

* **Depositar (`[d]`)**: Realiza um depósito em uma conta existente.
* **Sacar (`[s]`)**: Realiza um saque, respeitando o limite por transação e o limite diário de saques por conta.
* **Ver Extrato (`[e]`)**: Exibe o histórico de transações de uma conta.
* **Novo Usuário (`[nu]`)**: Permite o cadastro de novos clientes (Pessoa Física).
* **Nova Conta (`[nc]`)**: Cria uma nova conta corrente vinculada a um cliente existente.
* **Listar Contas (`[lc]`)**: Exibe todas as contas cadastradas no sistema.
* **Sair (`[q]`)**: Encerra a aplicação
