# Classes em python

class Pessoa:
    # Construtor
    # self faz referência ao objeto
    def __init__(self, nome, sobrenome='Silva'):
        self.nome = nome
        self.sobrenome = sobrenome

    # Criando outros métodos
    def apresentar(self):
        print(f'Nome: {self.nome} {self.sobrenome}')

# Criando uma subclasse de Pessoa
class Aluno(Pessoa):
    def __init__(self, nome, sobrenome,matricula):
        super().__init__(nome,sobrenome)
        self.matricula = matricula

    # Polimorfismo sobrescrevendo o método apresentar de Pessoa
    # O Overload não é implementado no python
    def apresentar(self):
        print(f'Nome: {self.nome} {self.sobrenome}')
        print(f'Matrícula: {self.matricula}')



def main():
    pessoa = Pessoa('Jonas','Silva')
    pessoa.apresentar()
    pessoa.nome = 'Ana'
    pessoa.apresentar()

if __name__ == '__main__':
    main()