#pratica biblioteca math
from math import sqrt, ceil
num = int(input('digite um número: '))
raiz = sqrt(num)
print('a raiz de {} é igual a {}' . format(num, ceil(raiz)))

# ou

import math
num = int(input('digite um número: '))
raiz = math.sqrt(num)
print('a raiz de {} é igual a {}' . format(num, math.trunc(raiz)))

# prática biblioteca random
# gera um número aleatório entre 0 e 1
import random
num = random.random()
print(num)

# gera um número inteiro aleatório entre 1 e 10
num = random.randint(1, 10)
print(num)

# Math : import math (importa tudo) ou from math import sqrt (importa especifico)
# ceil : arredonda para cima
# floor : arredonda para baixo
# trunc : apaga apos a virgula
# pow : potencia
# sqrt : calculo raiz quadrada
# factorial: calculo fatorial
