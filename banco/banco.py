class Banco:
    def __init__(self):
        self._contas = []

    def adicionar_conta(self, conta):
        self._contas.append(conta)

    def listar_contas(self):
        for conta in self._contas:
            print(f"Conta: {conta._numero} | Cliente: {conta._cliente.get_nome()}")

    def buscar_conta(self, numero):
        for conta in self._contas:
            if conta._numero == numero:
                return conta
        return None