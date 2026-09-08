nomes = []
medias = []

resp = 's'

while resp=='s':
    nome = input('Qual o nome: ')
    # o comando append() é responsável por adicionar elementos no final da lista
    # cria novos espaços como nos ArrayList
    nomes.append(nome)
    n1 = float(input('N1: '))
    n2 = float(input('N2: '))
    n3 = float(input('N3: '))
    media = (n1+n2+n3)/3
    medias.append(media)
    resp = input('Continuar s - sim n - não').lower()

for i in range(len(nomes)):
    print(f'Aluno {nomes[i]} tem média {medias[i]:.2f}')

