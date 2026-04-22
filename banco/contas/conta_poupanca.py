from contas.conta import Conta

class ContaPoupanca(Conta):
    def __init__(self, numero, cliente):
        super().__init__(numero, cliente)

    def sacar(self, valor):
        if valor <= 0:
            print("Valor inválido.")
            return

        if valor > self._saldo:
            print("Saldo insuficiente.")
            return

        self._saldo -= valor
        self._historico.adicionar_operacao(f"Saque Poupança: R${valor:.2f}")
        print("Saque realizado (Poupança)")