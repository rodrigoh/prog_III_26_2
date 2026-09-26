def soma(*valores):
    print(valores)
    return sum(valores)

def apresentar(**dados):
    for nome, valor in dados.items():
        print(f'{nome} => {valor}')

def trocar(a, b):
    c = a
    a = b
    b = c
    return a,b

print(soma(1,2,3,4,5))

apresentar(nome='Jonas', altura=1.8)
a,b = 10,5
c,d = trocar(a,b)
print(trocar(c,d))

# Trocando dois valores diretamente
b,a = a,b
print(a,b)