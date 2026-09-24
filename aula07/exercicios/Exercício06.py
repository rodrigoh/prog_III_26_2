'''
6. Coordenadas
Crie uma tupla contendo as coordenadas de um ponto:
ponto = (10, 25)
Faça um programa que determine em qual quadrante o ponto está:
1º quadrante
2º quadrante
3º quadrante
4º quadrante
eixo X
eixo Y
origem
'''

coordenada = input('Digite uma coordenada no formato x,y: ')

# Podemos usar a função split para quebrar a string em duas
# Em seguida usamos a função map para converter os dois valores resultantes em int
x,y = map(int,coordenada.split(','))

ponto = (x,y)

if x==0 and y==0:
    print(f'O ponto {ponto} fica na origem')
elif x==0:
    print(f'O ponto {ponto} fica sobre o eixo y')
elif y==0:
    print(f'O ponto {ponto} fica sobre o eixo x')
elif x>0 and y>0:
    print(f'O ponto {ponto} fica no primeiro quadrante')
elif x<0 and y>0:  # também funciona x < 0 < y
    print(f'O ponto {ponto} fica no segundo quadrante')
elif x<0 and y<0:
    print(f'O ponto {ponto} fica no terceiro quadrante')
else:
    print(f'O ponto {ponto} fica no quarto quadrante')