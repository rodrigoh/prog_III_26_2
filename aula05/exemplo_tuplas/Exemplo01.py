# declarando uma tupla
numero = (1,2,3,4,5)

# tuplas com um valor
n = (37,)

# tupla mista
li = [1,2,3]

# Assim podemos criar uma cópia da lista para dentro da tupla
# mista = (1,'Jonas',True, 1.8,li.copy())

mista = (1,'Jonas',True, 1.8,li)

print(mista)

li[1] = 100
print(mista)


# Usando o -1 acessamos o último elemento funciona para listas também

# len(numero)-1
print(numero[-1])

# Somando duas tuplas

p1 = (0,2)
p2 = (3,4)

pontos = p1 + p2
print(pontos)

# Temos uma nova tupla com 4 vezes a p2
repetida = p2*4