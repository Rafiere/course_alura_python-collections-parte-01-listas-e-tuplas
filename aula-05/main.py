# Outros builtins:

idades = [15, 87, 65, 56, 32, 49, 37]

# Estamos criando um range de 0 até 8.
range(len(idades)) # Lazy

for i in range(len(idades)):
    print(i, idades[i])


enumerate(idades) # Lazy

list(range(len(idades))) #Não é lazy, estamos forçando a geração dos valores

for valor in enumerate(idades):
    print(valor)