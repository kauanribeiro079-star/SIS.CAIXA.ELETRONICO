class Cliente:
    def __init__(self, nome, cpf):
        
        self._nome = nome
        self._cpf = cpf

    def get_nome(self):
        return self._nome

    def get_cpf(self):
        return self._cpf