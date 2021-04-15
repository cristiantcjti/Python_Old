from abc import ABCMeta, abstractmethod # Quando queremos forca esse method em todas as classes filhas mas não implementamos na classe pai.

class Conta(ABCMeta): # # Quando queremos forca esse method em todas as classes filhas mas não implementamos na classe pai.
    def __init__(self, conta):
        self._conta = conta
        self._saldo = 0

    @abstractmethod # Quando queremos forca esse method em todas as classes filhas mas não implementamos na classe pai.
    def passa_o_mes(self):
        pass

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return f"[Conta ({self._conta}) Saldo({self._saldo})]"

class ContaCorente(Conta):
    def passa_o_mes(self):
        self._saldo -= 2


class ContaPoupanca(Conta):
    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3

conta16 = ContaCorente(16)
conta16.deposita(1000)
conta16.passa_o_mes()
print(conta16)

conta17 = ContaPoupanca(17)
conta17.deposita(1000)
conta17.passa_o_mes()
print(conta17)


#Polymorrphism
conta16 = ContaCorente(16)
conta16.deposita(1000)
conta17 = ContaPoupanca(17)
conta17.deposita(1000)

contas = [conta16, conta17]

for conta in contas:
    conta.passa_o_mes() # duck typing
    print(conta)