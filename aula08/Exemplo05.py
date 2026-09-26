palavra ='aula de programação'

print(palavra.upper())
print(palavra.lower())
print(palavra.capitalize())
print(palavra.title())

palavra = '     teste    '
print(palavra.rstrip())

palavra ='aula de programação'
posicao = palavra.find('de')
print(posicao)

palavra = palavra.replace('de', 'por')

print(palavra.split(' '))

print()