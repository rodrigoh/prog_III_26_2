# for do python
# importante lembrar que o teste seria i<10
for i in range(10):
  print(i,end=' ')

print('\nOutro exemplo usando os demais parâmetros do range')

# a função range recebe três parâmetros
# (inicio, fim, passo)
for i in range(2,20,2):
  print(f'{i} ',end='')

print('\nOutro exemplo usando os dois primeiros parâmetros')

# podemos usar apenas os dois primeiros parâmetros, então ele usa passo 1 (padrão)
for i in range(-10, 5):
  print(i,end=' ')