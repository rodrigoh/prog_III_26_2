'''
3. Removendo valores repetidos
Dada a lista:
numeros = [4, 7, 4, 2, 9, 7, 1, 2, 9, 5, 4]
Crie uma nova lista contendo apenas os valores que aparecem uma única vez na lista resultante, mantendo a ordem da primeira ocorrência.
'''

# Se o objetivo for ter apenas os valores que aparecem apena uma vez
# O enunciado está confuso

numeros = [4, 7, 4, 2, 9, 7, 1, 2, 9, 5, 4]

unicos = [n for n in numeros if numeros.count(n)==1]

print(numeros)
print(unicos)