from contas.conta import Conta

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500):
        super().__init__(numero, cliente)
        self._limite = limite

    def sacar(self, valor):
        if valor <= 0:
            print("Valor inválido.")
            return

        if valor > (self._saldo + self._limite):
            print("Limite insuficiente.")
            return

        self._saldo -= valor
        self._historico.adicionar_operacao(f"Saque CC: R${valor:.2f}")
        print("Saque realizado (Conta Corrente)")