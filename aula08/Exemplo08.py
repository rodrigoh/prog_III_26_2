def soma(n1, n2):
    return n1 + n2

def apresentar(nome='Convidado', altura=1.8):
    '''Esta função serve para apresentar uma pessoa'''
    print(f'Nome: {nome}')
    print(f'Altura: {altura:.2f}')



# Função principal
v1 = int(input('Valor 1: '))
v2 = int(input('Valor 2: '))

resp = soma(v1,v2)
print(resp)

# Assume o valor padrão da função
apresentar()

# Uso os valores passados como parâmetro
apresentar('Jonas',1.7)

# Trocar a ordem dos parâmetros
apresentar(altura=1.6, nome='Pedro')

# Consultando a documentação da função
print(apresentar.__doc__)