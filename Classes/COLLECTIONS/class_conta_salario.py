from operator import attrgetter # busca variável privada dentro da classe
from functools import total_ordering

@total_ordering # apos definir __eq__ e qualquer outra def de comparação ex __lt__ esse decorator carrega os outros comparadores <= >=....
class ContaSalario:
  
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0
    
    def __eq__(self, outro):
        if type(outro) != ContaSalario:
            return False
        
        return self._codigo == outro._codigo and self._saldo == outro._saldo
    
    def deposita(self, valor):
        self._saldo += valor
    
    def __lt__(self, outro): # lessthan para comparar classes
        if self._saldo != outro._saldo:
            return self._saldo < outro._saldo
        return self._codigo < outro._outro

    def deposita(self, valor):
        self._saldo += valor
        
    def __str__(self):
        return f'[ Conta {self._codigo} Saldo {self._saldo}]'

conta1 = ContaSalario(123)
conta1.deposita(100)
conta2 = ContaSalario(123)

print(isinstance(ContaSalario(65), ContaSalario))

print(conta1 == conta2)


conta_do_guilherme = ContaSalario(17)
conta_do_guilherme.deposita(500)

conta_da_daniela = ContaSalario(3)
conta_da_daniela.deposita(1000)

conta_do_paulo = ContaSalario(133)
conta_do_paulo.deposita(510)

contas = [conta_do_guilherme, conta_da_daniela, conta_do_paulo]

conta_do_guilherme < conta_da_daniela

conta_do_guilherme > conta_da_daniela

for conta in sorted(contas):
  print(conta)

for conta in sorted(contas,reverse=True):
  print(conta)

for conta in sorted(contas, key=attrgetter("_saldo")): 
  print(conta)

print('Testando total order:',conta_do_guilherme <= conta_da_daniela)

