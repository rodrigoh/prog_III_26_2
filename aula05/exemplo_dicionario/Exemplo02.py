texto = input('Digite um texto: ').lower().replace(' ','')

letras = {}

for letra in texto:
    if letra in letras:
        letras[letra] = letras[letra]+1
    else:
        letras[letra] = 1

print(letras)