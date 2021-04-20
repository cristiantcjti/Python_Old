
idades = [15, 87, 32, 65, 56, 32, 49, 37]

for i in range(len(idades)):
  print(i, idades[i])

range(len(idades)) # lazy...

enumerate(idades) # lazy

list(range(len(idades))) # forcei a geração dos valores

list(enumerate(idades))

for indice, idade in enumerate(idades): # unpacking da nossa tupla
  print(indice, "x", idade)

usuarios = [
    ("Guilherme", 37, 1981),
    ("Daniela", 31, 1987),
    ("Paulo", 39, 1979)
]

for nome, idade, nascimento in usuarios: # ja desempacotando
  print(nome)

for nome, _, _ in usuarios: # ja desempacotando, ignorando o resto
  print(nome)