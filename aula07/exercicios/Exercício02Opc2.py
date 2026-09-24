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
pares = [n for n in numeros if n%2==0]
impares = [n for n in numeros if n%2!=0]

print('Números:',numeros)
print('Pares:',pares)
print('Ímpares:',impares)