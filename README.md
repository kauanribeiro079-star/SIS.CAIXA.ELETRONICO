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

## COMO USAR O SISTEMA (EXEMPLO): 
EXEMPLO DE UTILIZAÇÃO NO TERMINAL:

No terminal digite o seguinte comando para iniciar o código: 
```
python main.py
```

O sistema irá apresentar o seguinte menu: 
```
1 - Criar Conta
2 - Depositar
3 - Sacar
4 - Saldo
5 - Histórico
0 - Sair
```
PASSO 1: CRIAR UMA CONTA (Digite: 1, informe o Nome, CPF e escolha o tipo da conta)
```
Escolha: 1
Nome: Kauan
CPF: 123
1 - CONTA CORRENTE | 2 - CONTA POUPANÇA: 1
```
Saída: 
```
Conta Criada!
```
PASSO 2: DEPOSITAR DINHEIRO (Digite: 2 e como é a primeira conta, a conta será: 1)
```
Escolha: 2 
Conta: 1
Valor: 500 
```
Saída: 
```
Depósito realizado! 
```
PASSO 3: SACAR DINHEIRO (Digite: 3 e a Conta: 1)
```
Escolha: 3 
Conta: 1 
Valor: 200
```
Saída: 
```
Saque realizado (Conta Corrente)
```
PASSO 4: CONSULTAR SALDO (Digite: 4 e Conta: 1)
```
Escolha: 4
Conta: 1
```
Saída: 
```
Saldo: R$300.00
```
PASSO 5: VISUALIZAR HISTÓRICO (Digite: 5 e Conta:1)
```
Escolha: 5
Conta:1
```
Saída:
```
Histórico de operações:
- Depósito: R$500.00
- Saque CC: R$200.00
```

OBSERVAÇÕES:
* O número da conta é gerado automaticamente (1, 2, 3, ...)
* Todas as operações são registradas no histórico
* O sistema valida saldo antes de permitir o saque

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

## REGRAS DO SISTEMA:

* Não permite saque com saldo insuficiente
* Todas as operações são registradas no histórico
* Entradas do usuário são validadas
* O sistema exibe mensagens claras no terminal

---

## AUTOR

Kauan Ribeiro de Siqueira


Bacharelado em Ciência da Computação - IFCE
