# Precisamos importar o Counter
from collections import Counter

lista = [1,2,3,4,5,3,4,5]


cont = Counter(lista)

print(cont)
# Counter({3: 2, 4: 2, 5: 2, 1: 1, 2: 1})

palavra = 'banana'

cont = Counter(palavra)

print(cont)

cont.update('abacaxi')

print(cont)

