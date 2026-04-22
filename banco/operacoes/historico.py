class Historico:
    def __init__(self):
        # lista
        self._operacoes = []

    def adicionar_operacao(self, descricao):
        # adicionar no histórico
        self._operacoes.append(descricao)

    def mostrar(self):
        print("\n Histórico de operações:")
        if not self._operacoes:
            print("Nenhuma operação realizada.")
        else:
            for op in self._operacoes:
                print(f"- {op}")