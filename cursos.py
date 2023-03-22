usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_learn = {13, 23, 56, 42}

print("Conjunto Usuários Data Science")
print(usuarios_data_science)
print("\n")

print("Conjunto Usuários Machine Learn")
print(usuarios_machine_learn)

print("União dos Conjuntos")
print(usuarios_data_science | usuarios_machine_learn)

print("Intersection dos Conjuntos")
print(usuarios_data_science & usuarios_machine_learn)

print("Usuários que estão no Data Science mas não estão no Machine Learn")
print(usuarios_data_science - usuarios_machine_learn)

print("Operação de OU Exclusivo")
print(usuarios_data_science ^ usuarios_machine_learn)

usuarios = {1, 5, 76, 34, 52, 13, 17}
len(usuarios)

usuarios.add(13)
len(usuarios)

usuarios.add(765)
len(usuarios)

usuarios

# 'Congelando estado do meu conjunto'
usuarios = frozenset(usuarios)
usuarios

type(usuarios)

#usuarios.add(134)

meu_texto = "Bem vindo meu nome é Wellington, eu gosto muito de cachorros, cachorros são vida"
meu_texto.split()

set(meu_texto.split())

print(set(meu_texto.split()))
