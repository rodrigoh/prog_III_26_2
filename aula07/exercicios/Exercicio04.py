'''
4. Rotação de lista
Crie uma lista com 8 números.
Faça um programa que mova o último elemento para o início da lista.
Exemplo:
Original: [10, 20, 30, 40, 50]
Resultado: [50, 10, 20, 30, 40]
'''

original = [10, 20, 30, 40, 50]

invertida = []

for i in range(len(original)-1, -1, -1):
    invertida.append(original[i])

print(original)
print(invertida)