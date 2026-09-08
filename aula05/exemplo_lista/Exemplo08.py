import random

li = []

# Desta forma podemos usam em qualquer linguagem de programação
for i in range(10):
    num = random.randint(1,100)
    li.append(num)

print(li)

# Desta forma temos o mesmo resultado, porém usando a sintaxe
# do python
# [o_que_fazer por_quantas_vezes]
lista = [random.randint(1,20) for i in range(20)]

print(lista)

# apagando todos os elementos de uma lista
lista.clear()

# alternativamente podemos:
lista = []

print(lista)

# Podemos usar o copy para fazer uma cópia da lista
lb = lista.copy()

lb = [2,3,4,5,6]

# Permite remover um elemento da lista, semelhante ao del
lb.pop(2)
