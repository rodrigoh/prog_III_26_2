'''
3. Removendo valores repetidos
Dada a lista:
numeros = [4, 7, 4, 2, 9, 7, 1, 2, 9, 5, 4]
Crie uma nova lista contendo apenas os valores que aparecem uma única vez na lista resultante, mantendo a ordem da primeira ocorrência.
'''
numeros = [4, 7, 4, 2, 9, 7, 1, 2, 9, 5, 4]

unicos = []

for i in numeros:
    if i not in unicos:
        unicos.append(i)

print(numeros)
print(unicos)