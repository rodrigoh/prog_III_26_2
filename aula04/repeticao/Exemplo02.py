# leia uma nota do teclado e garanta que esteja entre 1 e 10

nota = float(input('Qual a nota do aluno: '))
while nota < 1 or nota > 10:
  nota = float(input('A nota precisa estar entre 1 e 10: '))

# neste caso não usamos o if porque ele irá repetir a leitura da nota apenas uma vez
# nota = float(input('Qual a nota do aluno: '))
# if nota<1 or nota>10:
#   nota = float(input('A nota precisa estar entre 1 e 10: '))
