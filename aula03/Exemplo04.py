v1 = int(input('Qual o primeiro valor: '))
v2 = int(input('Qual o segundo valor: '))

r = v1 / v2
print(f'A divisão de {v1} por {v2} vale {r}')

r = v1 // v2 
print(f'A divisão inteira de {v1} por {v2} vale {r}')

r = v1 % v2 
print(f'O resto da divisão inteira de {v1} por {v2} vale {r}')

# exponenciação
r = v1 ** v2
print(f'{v1} elevado a {v2} vale {r}')

# exponenciação
r = pow(v1,v2)
print(f'{v1} elevado a {v2} vale {r}')

v1 //= v2
print(f'A divisão inteira pode ser usar com atribuição simplificada {v1}')