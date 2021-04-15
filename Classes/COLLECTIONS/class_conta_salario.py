class ContaSalario():
    def __init__(self, conta):
        self._conta = conta
        self._saldo = 0

    def __eq__(self, outra): # define a condicao de igualdade
        return self._conta == outra._conta and self._saldo == outra._saldo

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return f'[ Conta {self._conta} Saldo {self._saldo}]'

conta1 = ContaSalario(123)
conta1.deposita(100)
conta2 = ContaSalario(123)

print(isinstance(ContaSalario(65), ContaSalario))

print(conta1 == conta2)

