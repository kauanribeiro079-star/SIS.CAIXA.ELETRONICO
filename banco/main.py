from clientes.cliente import Cliente
from contas.conta_corrente import ContaCorrente
from contas.conta_poupanca import ContaPoupanca
from banco import Banco

banco = Banco()

while True:
    print("\n1 - Criar Conta")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Saldo")
    print("5 - Histórico")
    print("0 - Sair")

    op = input("Escolha: ")

    if op == "1":
        nome = input("Nome: ")
        cpf = input("CPF: ")
        tipo = input("1- C.Corrente | 2- C.Poupança: ")

        cliente = Cliente(nome, cpf)
        numero = len(banco._contas) + 1

        if tipo == "1":
            conta = ContaCorrente(numero, cliente)
        else:
            conta = ContaPoupanca(numero, cliente)

        banco.adicionar_conta(conta)
        print("Conta criada!")

    elif op == "2":
        num = int(input("Conta: "))
        conta = banco.buscar_conta(num)
        if conta:
            valor = float(input("Valor: "))
            conta.depositar(valor)

    elif op == "3":
        num = int(input("Conta: "))
        conta = banco.buscar_conta(num)
        if conta:
            valor = float(input("Valor: "))
            conta.sacar(valor)

    elif op == "4":
        num = int(input("Conta: "))
        conta = banco.buscar_conta(num)
        if conta:
            conta.consultar_saldo()

    elif op == "5":
        num = int(input("Conta: "))
        conta = banco.buscar_conta(num)
        if conta:
            conta.mostrar_historico()

    elif op == "0":
        break