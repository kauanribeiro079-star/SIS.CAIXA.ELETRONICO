from operacoes.historico import Historico

class Conta:
    def __init__(self, numero, cliente):
        self._numero = numero
        self._cliente = cliente
        self._saldo = 0.0
        self._historico = Historico()

    def get_saldo(self):
        return self._saldo

    def depositar(self, valor):
        if valor <= 0:
            print("Valor inválido.")
            return

        self._saldo += valor
        self._historico.adicionar_operacao(f"Depósito: R${valor:.2f}")
        print("✅ Depósito realizado!")

    def sacar(self, valor):
        if valor <= 0:
            print("Valor inválido.")
            return

        if valor > self._saldo:
            print("Saldo insuficiente.")
            return

        self._saldo -= valor
        self._historico.adicionar_operacao(f"Saque: R${valor:.2f}")
        print("Saque realizado!")

    def consultar_saldo(self):
        print(f" Saldo: R${self._saldo:.2f}")

    def mostrar_historico(self):
        self._historico.mostrar()