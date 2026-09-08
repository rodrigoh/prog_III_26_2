# criando um dicionário
aluno = {
    'nome':'Jonas',
    'notas':[8,9,10],
    'curso':'TI',
    'idade':18,
    'e_mail':'jonas@gmail.com'
}

# Imprimindo o dicionário
print(aluno)

# Acessando uma chave
print('Nome: ',aluno['nome'])
print('Idade: ',aluno['idade'])
print('Notas: ',aluno['notas'])
print('Teste: ',aluno.get('teste','A chave teste não existe'))

# adicionando uma nova chave
aluno['status'] = 'Aprovado'

print(aluno)

# Removendo uma chave do dicionário
aluno.pop('nome')
print(aluno)

del aluno['notas']
print(aluno)

chaves = aluno.keys()
valores = aluno.values()
print('\nIterando as chaves do dicionário')
for i in aluno.keys():
    print(i,end=' ')

print('\nIterando os values do dicionário')
for i in aluno.values():
    print(i,end=' ')

print('\nIterando os dois ao mesmo tempo')
for chave, valor in aluno.items():
    print(f'{chave} : {valor}')

print('\nAtualizando o conteúdo')

aluno.update({'nome':'Jonas','curso':'Informática'})

print(aluno)

aluno['curso'] = 'TI'

