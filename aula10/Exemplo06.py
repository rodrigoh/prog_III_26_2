class Operacoes:
    # Criando um atributo de classe
    pi = 3.14159265359

    # Método simples
    def soma(self, n1, n2):
        return n1 + n2

    # Criando um método de classe
    # cls = class, estamos acessando um atributo de classe
    @classmethod
    def valor_pi(cls):
        return cls.pi

    # Criando um método estático
    # O método não recebe o self
    @staticmethod
    def dividir(n1, n2):
        if n2==0:
            raise ZeroDivisionError('Não podemos dividir por zero')
        return n1/n2

