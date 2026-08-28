'''
Operadores relacionais

> -> maior que
< -> menor que
>= -> maior ou igual
<= -> menor ou igual
== -> igual
!= -> diferente

Operadores lógicos

and -> E lógico &&
or -> OU lógico ||
not -> Não lógico !
'''

numero = int(input('Digite um número: '))

if numero == 0:
  print(f'O valor {numero} é zero')
elif numero > 0:
  print(f'O valor {numero} é positivo')
else:
  print(f'O valor {numero} é negativo')