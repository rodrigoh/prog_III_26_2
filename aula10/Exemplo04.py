
class Pessoa:
    def __init__(self, nome):
        #Definindo um atributo como privado
        # Sem nenhum modificador é publico
        # _ é protegido
        # __ é privado
        self.__nome = nome

    def get_nome(self):
        return self.__nome

    def set_nome(self,nome):
        if len(nome)>0:
            self.__nome = nome

    # Estamos criando o getter
    @property
    def nome(self):
        return self.__nome

    # Criando um setter
    @nome.setter
    def nome(self,nome):
        if len(nome)>0:
            self.__nome = nome


pessoa = Pessoa('Jonas')
# O acesso ao atributo é transparente
pessoa.nome = 'Ana'
print('O nome da pessoa é',pessoa.nome)
