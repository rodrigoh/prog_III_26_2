'''
9. Agenda telefônica
Crie um programa que mantenha uma agenda utilizando um dicionário:
agenda = {
    "Ana": "51999999999",
    "Carlos": "51988888888",
    "Maria": "51977777777"
}
O programa deve apresentar um menu:
1 - Adicionar contato
2 - Buscar contato
3 - Alterar telefone
4 - Remover contato
5 - Listar contatos
0 - Sair
'''

agenda = {
    "Ana": "51999999999",
    "Carlos": "51988888888",
    "Maria": "51977777777"
}

opc = 1

while opc!=0:
    print('Selecione uma opção')
    print('1 - Adicionar contato')
    print('2 - Buscar contato')
    print('3 - Alterar telefone')
    print('4 - Remover contato')
    print('5 - Listar contatos')
    print('0 - Sair')
    opc = int(input(': '))
    match opc:
        case 1:
            nome = input('Qual o nome do novo contato: ')
            telefone = input(f'Qual o telefone do {nome}: ')
            agenda[nome] = telefone
        case 2:
            # capitalize() -> primeira letra em maiúscula
            nome = input('Qual o nome do novo contato: ').capitalize()
            print(agenda.get(nome,'Contato não encontrado'))
        case 3:
            nome = input('Qual o nome do contato para alterar: ').capitalize()
            telefone = input(f'Qual o novo telefone do {nome}: ')
            agenda[nome] = telefone
        case 4:
            nome = input('Qual o nome do contato para deletar: ').capitalize()
            if nome in agenda:
                agenda.pop(nome)
            else:
                print(f'Contato {nome} não localizado')
        case 5:
            print(agenda)
