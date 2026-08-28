# Leia um número do teclado, garanta que ele esteja entre 1 e 10, após 
# imprima a sua tabuada usando while

numero = int(input('Informe um número entre 1 e 10: '))

while numero<1 or numero>10:
  numero = int(input('Eu disse entre 1 e 10: '))

i = 1

while i<=10:
  mult = i * numero
  print(f'{numero} x {i} = {mult}')
  i += 1