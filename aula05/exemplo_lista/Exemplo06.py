li = [1,2,3,4,5,6,7]

# lista de string
nomes = ["Jonas", 'Ana', 'Pedro']

# Remove um elemento pela posição
del li[3]

# Aqui removemos os elementos do índice 2 até o 4
del li[2:5]

print(li)

# Removendo um elemento pelo elemento
nomes.remove('Ana')
print(nomes)

# Ordenando uma lista
li = [1,6,1,0,7,9,10,4,3]

# Ordem crescente
print("\nOrdem crescente")
li.sort()
print(li)

# Ordem decrescente
print("\nOrdem decrescente")
li.sort(reverse=True)
print(li)

# Invertendo a ordem dos elementos
li = [1,6,1,0,7,9,10,4,3]
li.reverse()
print('Invertendo a ordem dos elementos')
print(li)



