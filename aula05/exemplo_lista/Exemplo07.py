li = [1,3,4,5,6]

# É possível adicionar um elemento a qualquer posição da lista
# Usando o insert(posição, elemento)
print(li)

li.insert(1,2)

print(li)

lb = [6,7,8]

li.insert(2,lb)

print(li)

# Contando os elementos de uma lista

li = [1,2,3,4,4,5,6,4,3]

print('Quantos números 3 tenho na lista',li.count(3))
print('Quantos números 10 tenho na lista',li.count(10))

nome = 'Jonas Silva'

lista = list(nome.lower())

print(f'O nome {nome} tem {lista.count('a')} letras a')

# Descobrir a posição de um elemento na lista

print(f'O primeiro a em {nome} aparece na posição {lista.index('a')}')