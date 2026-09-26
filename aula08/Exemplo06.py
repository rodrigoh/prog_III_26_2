try:
    n1 = int(input('N1: '))
    n2 = int(input('N2: '))
    resultado = n1//n2
    print(resultado)
except ZeroDivisionError:
    print('Não pode dividir por zero')