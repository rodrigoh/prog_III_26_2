# Podemos incluir o arquivo inteiro
# O as funcoes
import Exemplo01 as funcoes

# Importando apenas uma função
# O as soma
from Exemplo01 import soma_elementos as soma

# Podemos incluir arquivos de diferentes, mas precisamos usar o caminho relativo
import aula08.Exemplo10 as exemplo

#from aula08.Exemplo10 import soma

print(funcoes.soma_elementos(6,7,2))

print(soma(6,7,2))

