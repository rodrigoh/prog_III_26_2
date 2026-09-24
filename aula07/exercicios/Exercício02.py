'''
2. Separando pares e ímpares
Dada a lista:
numeros = [12, 7, 25, 8, 14, 33, 10, 5, 18, 21]
Crie duas novas listas:
uma contendo apenas os números pares;
outra contendo apenas os números ímpares.
Ao final, exiba as três listas.
'''
numeros = [12, 7, 25, 8, 14, 33, 10, 5, 18, 21]
pares = []
impares = []

for i in numeros:
    if i%2==0:
        pares.append(i)
    else:
        impares.append(i)

# for i in range(len(numeros)):
#     if numeros[i]%2==0:
#         pares.append(numeros[i])
#     else:
#         impares.append(numeros[i])

print('Números:',numeros)
print('Pares:',pares)
print('Impares:',impares)
