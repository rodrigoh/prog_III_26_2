
valor = 5

def soma(n1,n2):
    global valor
    valor = 10
    return n1+n2+valor


def main():
    print(valor)
    print(soma(1, 2))

    print(valor)

if __name__ == '__main__':
    main()