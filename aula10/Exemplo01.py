# Funções em python
def soma_lista(lista):
    soma = 0
    for i in lista:
        soma+=i
    return soma

# Uma função que recebe uma quantidade variável de parâmetros
# soma_elementos(3,5,6,1,2)
def soma_elementos(*valores):
    '''Os elementos recebidos são pela função em formato de tupla'''
    print(f'Elementos recebidos pela função: {valores}')
    soma = 0
    for i in valores:
        soma+=i
    return soma

# Recebendo uma quantidade parâmetros nomeados variáveis
# apresentar(nome='Jonas', idade=23, altura=1.8)
def apresentar(**dados):
    '''Recebe os parâmetros nomeados como um dicionário'''
    print(dados)
    for chave, valor in dados.items():
        print(f'{chave}:{valor}')


def apresentar_dois(nome='Pessoa', e_mail='pessoa@email.com', idade=20):
    print('Nome:',nome)
    print('E-mail:',e_mail)
    print('Idade:',idade)


def main():
    lista = [1,2,3,4,5,6]
    print('Usando a função que soma os elementos de uma lista')
    print(soma_lista(lista))

    print('Usando a função que soma n elementos')
    print(soma_elementos(5,9,7,10))
    print('A documentação da função soma_elementos é',soma_elementos.__doc__)

    print('Chamando a função que recebe n parâmetros nomeados')
    apresentar(nome='Ana',e_mail='ana@email.com')
    apresentar(nome='Jonas',idade=20,notas=[8,9,10])

    print('Chamando a outra função')
    apresentar_dois()
    apresentar_dois('Jonas','jonas@email.com',20)
    apresentar_dois(e_mail='jonas@email.com')
    apresentar_dois(e_mail='jonas@email.com', idade=25, nome='Jonas')


if __name__ == '__main__':
    main()

