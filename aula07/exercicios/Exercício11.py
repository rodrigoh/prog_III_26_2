'''
11. Cadastro de alunos
Utilize um dicionário contendo listas:
alunos = {
    "Ana": [8.5, 7.0, 9.0],
    "Carlos": [6.0, 5.5, 7.0],
    "Maria": [9.5, 9.0, 10.0]
}
Calcule a média de cada aluno e informe:
Ana → 8.17 → Aprovada
Carlos → 6.17 → Aprovado
Maria → 9.50 → Aprovada
'''

alunos = {
    "Ana": [8.5, 7.0, 9.0],
    "Carlos": [6.0, 5.5, 7.0],
    "Maria": [9.5, 9.0, 10.0]
}

for nome, notas in alunos.items():
    media = sum(notas)/len(notas)
    print(f'{nome} tem média {media:.2f}',end=' ')
    if media>=6:
        print('aprovado')
    else:
        print('reprovado')
