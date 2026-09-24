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

# Podemos gerar uma lista diretamente com o comando
lista = [random.randint(1,100) for i in range(10)]

maior = max(lista)
menor = min(lista)
media = sum(lista)/len(lista)

soma = 0

print(f'Lista: {lista} maior número: {maior} e o menor número: {menor} e a média {media:.2f}')