class ContaCorrente:
    def __init__(self, conta):
        self.conta = conta
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return f"[Conta ({self.conta}) Saldo({self.saldo})]"

conta_cris = ContaCorrente(123)
conta_dani = ContaCorrente(321)

contas = [conta_cris, conta_dani]

conta_cris.deposita(100)
conta_dani.deposita(200)

for conta in contas:
    print(conta)
