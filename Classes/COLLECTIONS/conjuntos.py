usuarios_data_science = [15, 23, 43, 56]
usuarios_machine_learning = [13, 23, 56, 42]

assistiram = usuarios_data_science.copy()
assistiram.extend(usuarios_machine_learning)
print(assistiram)

print(len(assistiram))

print(set(assistiram))

print(set([1,2,3,1]))

print({4, 1,2,3,1})

print(type({1,2}))

usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_learning = {13, 23, 56, 42}

print(usuarios_machine_learning)

 # print(usuarios_machine_learning[3]) não tem indice

for usuario in set(assistiram):
  print(usuario)

usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_learning = {13, 23, 56, 42}

print(usuarios_data_science | usuarios_machine_learning) # une dados unicos e exclui repetidos

print(usuarios_data_science & usuarios_machine_learning) # une dados duplicados

print(usuarios_data_science - usuarios_machine_learning) # une dados unicos

fez_ds_mas_nao_fez_ml = usuarios_data_science - usuarios_machine_learning
print(15 in fez_ds_mas_nao_fez_ml)

print(23 in fez_ds_mas_nao_fez_ml)

print(usuarios_data_science ^ usuarios_machine_learning) # ou exclusivo