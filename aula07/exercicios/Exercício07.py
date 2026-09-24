'''
7. Ranking de jogadores
Considere:
jogadores = (
    ("Ana", 1500),
    ("Carlos", 2100),
    ("João", 1800),
    ("Maria", 2400),
    ("Pedro", 1950)
)
Mostre:
o jogador com maior pontuação;
o jogador com menor pontuação;
a média das pontuações;
todos os jogadores com pontuação acima da média.
'''
from exercicios.Exercicio01Opc2 import menor

jogadores = (
    ("Ana", 1500),
    ("Carlos", 2100),
    ("João", 1800),
    ("Maria", 2400),
    ("Pedro", 1950)
)

maior_pontuacao = jogadores[0]
menor_pontuacao = jogadores[0]

soma = 0

for jogador in jogadores:
    if jogador[1]>maior_pontuacao[1]:
        maior_pontuacao = jogador
    if jogador[1]<menor_pontuacao[1]:
        menor_pontuacao = jogador
    soma+=jogador[1]

media = soma/len(jogadores)

print(f'O jogador com maior pontuação é {maior_pontuacao}')
print(f'O jogador com menor pontuação é {menor_pontuacao}')
print(f'A ponstuação média é {media:.2f} e estão acima dessa pontuação')
for jogador in jogadores:
    if jogador[1]>media:
        print(jogador)

