'''
Gerar listas
1. Maior e menor valor
Crie uma lista com 10 números inteiros.
Faça um programa que:
mostre a lista;
informe o maior número;
informe o menor número;
calcule a média dos valores.
Não use max e min
'''

import random

from main import print_hi

lista = []

maior = 0
menor = 0

soma = 0

for i in range(10):
    lista.append(random.randint(1,100))
    if i==0:
        maior = lista[i]
        menor = lista[i]
    else:
        if menor > lista[i]:
            menor = lista[i]
        if maior < lista[i]:
            maior = lista[i]
    soma+=lista[i]

media = soma/len(lista)

print(f'Lista: {lista} maior número: {maior} e o menor número: {menor} e a média {media:.2f}')