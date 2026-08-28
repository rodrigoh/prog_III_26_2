nome = input('Digite seu nome: ')
idade = int(input('Qual sua idade: '))
altura = float(input('Qual sua altura: '))

# Nesta linha estamos concatenando os vários objetos que vamos imprimir
print('Bem vindo',nome,'você tem',idade,'anos e mede',altura,'metros')

''' Nesta podemos usar {} para imprimir variáveis dentro da string 
 só não podemos esquecer do f antes da string
 para limitar o número de casas decimais usamos :.2f, sendo 2 o número de casas 
 decimais
'''
print(f'Bem vindo {nome} você tem {idade} anos e mede {altura:.2f} metros')
