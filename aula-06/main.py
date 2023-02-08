# Ordenação básica

idades = [15, 87, 32, 65, 56, 32, 49, 37]

# O método "sorted()" realiza a ordenação das idades, retornando uma lista com os valores ordenados. Essa
# ordenação é feita utilizando a comparação dos próprios números.
orderedList = sorted(idades)
print(orderedList)

# Caso queiramos a ordem contrária, podemos utilizar o parâmetro "reverse".
reversedOrderedList = sorted(idades, reverse=True)
print(reversedOrderedList)
