# como funciona o while
i = 0
print('\nContando de 0 a 9 com o while')
while i < 10:
    print(i,end=' ')
    i+=1

print('\nContando de 0 a 9 com o for')
for i in range(10):
    print(i, end=' ')

# A função range recebe três parâmetros
# inicial -> padrão é 0
# valor final -> até onde o for deve iterar, de certa forma o teste dele é < menor que
# passo -> o incremento da variável

print('\nFor com todos os parâmetros')
for i in range(10,0,-1):
    print(i, end=' ')

nome = input('\nQual seu nome: ')
# Se comporta como o para cada for(char letra : vetor)
for letra in nome:
    print(letra)
    print('...')
