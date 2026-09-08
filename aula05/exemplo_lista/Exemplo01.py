# Declarando a existência de uma lista
lista = []

# Declarar uma lista e adicionando elementos a ela
lista = [1,2,3,4,5]

print(lista)

# A iteração com os elementos da lista é igual
i = 0
print('\nIterando a lista com o while')
while i<5:
    print(lista[i],end=' ')
    i+=1

print('\nIterando a lista com o for...range()')
for i in range(5):
    print(lista[i], end=' ')

print('\nIterando a lista com o for')
for i in lista:
    print(i, end=' ')



