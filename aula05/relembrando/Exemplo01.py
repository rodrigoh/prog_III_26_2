# Como é o if
numero = int(input('Digite um número: '))

if numero==0:
    print('O número é zero')
elif numero>0:
    print(f'O número {numero} é positivo')
else:
    print(f'O número {numero} é negativo')

# switch case
dia = int(input('Digite um dia da semana: '))
match dia:
    case 1: print('É domingo')
    case 2: print('É segunda-feira')
    case 3: print('...')
    case _: print(f'O número {dia} não corresponde a nenhum dia da semana')
