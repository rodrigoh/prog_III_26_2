
from abc import ABC,abstractmethod

class Animal(ABC):
    def __init__(self,nome):
        self.nome = nome

    @abstractmethod
    def emitir_som(self):
        pass

class Cachorro(Animal):
    def __init__(self,nome):
        super().__init__(nome)
    def emitir_som(self):
        print(self.nome,'faz au au!')