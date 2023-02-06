# As coleções são vários elementos que estão unidos em uma estrutura.

idades = [39, 20, 27, 18]

print(type(idades))
print(idades[1])

print(len(idades))


# Adicionando o valor "15" a lista "idades".
idades.append(15)
print(idades)

idades.clear()
print(idades)

## Para sabermos se um elemento está em uma lista

print(15 in idades)
if 15 in idades:
    idades.remove(15)

idades.insert(0, 20)
print(idades)

# Estamos inserindo dois elementos ao mesmo tempo na lista.
idades.extend([27, 19])
print(idades)

# Estamos criando uma lista onde vamos passar o valor de idade somado com "1" para cada elemento dentro de "idades".
# Basicamente, para cada idade, vamos retornar uma nova lista com "idade" somado com "1".
print([(idade + 1) for idade in idades])

# Obtendo apenas as idades maiores que 21. O nome dessa sintaxe, que usa colchetes, é "list comprehension".
print([(idade) for idade in idades if idade > 21])

# É muito ruim utilizarmos objetos mutáveis, pois isso pode causar vários bugs.

# Sempre que passamos um objeto mutável como parâmetro, não sabemos o que podemos receber depois, pois, como
# ele é mutável, os valores dele podem ser alterados.
