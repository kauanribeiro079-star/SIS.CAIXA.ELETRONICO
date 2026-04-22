# SISTEMA DE CAIXA ELETRONICO

## SOBRE O PROJETO

Este projeto consiste na simulação de um sistema de caixa eletrônico, desenvolvido utilizando a linguagem de programação Python, com o objetivo de aplicar na prática os principais conceitos de Programação Orientada a Objetos (POO).

O sistema funciona via terminal e permite a realização de operações bancárias básicas.

---

## AS FUNCIONALIDADES DO PROGRMA CONSISTE: 

* Criar conta (Corrente ou Poupança)
* Depositar dinheiro
* Sacar dinheiro
* Consultar saldo
* Visualizar histórico de operações

---

## OS CONCEITOS DE POO FORAM APLICADOS:

* **Encapsulamento:** uso de atributos privados como `_saldo`
* **Herança:** `ContaCorrente` e `ContaPoupanca` herdam de `Conta`
* **Polimorfismo:** método `sacar()` com comportamentos diferentes
* **Composição:** a classe `Conta` possui um `Historico`
* **Agregação:** a classe `Banco` gerencia múltiplas contas

---

## A ESTRUTURA DO PROJETO É A SEGUINTE:

```
banco/
│
├── contas/
│   ├── conta.py
│   ├── conta_corrente.py
│   ├── conta_poupanca.py
│
├── clientes/
│   └── cliente.py
│
├── operacoes/
│   └── historico.py
│
├── banco.py
└── main.py
```
---

## EXEMPLO DE USABILIDADE DO SISTEMA

```
1 - Criar Conta
2 - Depositar
3 - Sacar
4 - Saldo
5 - Histórico
0 - Sair
```

---

## REGRAS DO SISTEMA:

* Não permite saque com saldo insuficiente
* Todas as operações são registradas no histórico
* Entradas do usuário são validadas
* O sistema exibe mensagens claras no terminal

---

## AUTOR

Kauan Ribeiro de Siqueira
Bacharelado em Ciência da Computação - IFCE
