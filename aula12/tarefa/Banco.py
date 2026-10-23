# Classe Conta
from operator import truediv


class Conta:
    # Criando o construtor
    def __init__(self,titular):
        # Criando um atributo privado
        self.__titular = titular
        self.__saldo = 0

    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self,titular):
        if len(titular)>0:
            self.__titular = titular
    # De certa forma o setter torna o acesso ao atributo transparente
    # conta = Conta('Jonas')
    # conta.titular = 'Ana'
    # print(conta.titular)

    def depositar(self,valor):
        if valor>0:
            self.__saldo+=valor

    def sacar(self,valor):
        #0 < valor <= self.__saldo
        if valor > 0 and valor <= self.__saldo:
            self.__saldo-=valor
            return True
        return False


    def verificar_saldo(self):
        return f'Seu saldo atual é R${self.__saldo:.2f}'


# Criando uma classe filha da classe Conta
class Corrente(Conta):
    def __init__(self,titular, limite):
        # Chamando o construtor da classe pai
        super().__init__(titular)
        self.__limite = limite
        self.__saldo = 0

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        if limite>0:
            self.__limite = limite

    def sacar(self,valor):
        if valor > 0 and valor <= self.__saldo + self.__limite:
            self.__saldo-=valor
            return True
        return False

    def verificar_saldo(self):
        resposta = f'Seu saldo atual é de R$ {self.__saldo:.2f}'
        if self.__saldo<0:
            resposta+=f'\nSeu limite disponível é de R$ {(self.__limite+self.__saldo):.2f}'
        else:
            resposta += f'\nSeu limite disponível é de R$ {self.__limite:.2f}'
        return resposta


def main():
    conta = Conta('Jonas')
    conta.depositar(100)
    if conta.sacar(50):
        print('Saque realizado')
        print('Seu novo saldo é de')
        print(conta.verificar_saldo())

    conta_corrente = Corrente('Ana',200)
    print('Bem vindo(a):',conta_corrente.titular)
    if conta_corrente.sacar(100):
        print('Saque realizado')
        print('Seu novo saldo é de ')
        print(conta_corrente.verificar_saldo())


if __name__ == '__main__':
    main()