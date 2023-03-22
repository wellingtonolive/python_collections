meu_texto = "Bem vindo meu nome é Wellington, eu gosto muito de cachorros, cachorros são vida"
meu_texto.split()

set(meu_texto.split())

print(set(meu_texto.split()))

aparicoes = {
    "Wellington": 1,
    "cachorro": 2,
    "nome": 2,
    "muito": 2
}

print("Procurando valor dentro do Dict")
response = "Zé" in aparicoes
print(response)

print("Iterando Dict: Somente as Chaves")
for elemento in aparicoes.keys():
    print(elemento)

print("Iterando Dict: Somente os Valores")
for elemento in aparicoes.values():
    print(elemento)

print("Iterando Dict: Chaves e Valores")
for elemento in aparicoes.keys():
    print(elemento, aparicoes[elemento])

print("Iterando Dict: Itens")
for elemento in aparicoes.items():
    print(elemento)

print("Iterando Dict: Desempacotando")
for key, valor in aparicoes.items():
    print(key, "=", valor)

print("Concatenando uma palavra para cada nome de chave e jogando numa lista")
print(["palavra {}".format(chave) for chave in aparicoes.keys()])
