try:
    arquivo = open('texte.txt')
    print(arquivo.encoding)
except FileNotFoundError as erro:
    print('Arquivo não localizado')
    print(erro)
finally:
    print('Arquivo fechado')