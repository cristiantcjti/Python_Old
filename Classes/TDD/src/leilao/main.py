from .dominio import Usuario, Lance, Leilao, Avaliador

cris = Usuario('cris')
paulo = Usuario('paulo')

lance_do_cris = Lance(cris, 100.0)
lance_do_paulo = Lance(paulo, 150.0)

leilao = Leilao('Celular')

leilao.lances.append(lance_do_cris)
leilao.lances.append(lance_do_paulo)

for lance in leilao.lances:
    print(f"O usuario {lance.usuario.nome} deu um lance de {lance.valor}")

avaliador = Avaliador()
avaliador.avalia(leilao)

print(f'O menor lance foi de {avaliador.menor_lance} e o maior lance for de {avaliador.maior_lance}')