'''

Breve análise:


Inicialmente escolhemos e printamos o número de cenários T de forma
aleatório em uma faixa de 0 a 5, também escolhida aleatóriamente.


Em seguida, definimos uma variável W para nos auxiliar na iteração dos
cenários, iteração esta feita pelo primeiro loop while.


Dentro do loop while a variável N, que será a dimensão da matriz
identidade quadrada, recebe um valor aleatoriamente. Esse valor
é printado.


Em seguida, definimos um valor t para receber a matriz quadrada
identidade, pela função eye(), importada do módulo numpy, que
cria matrizes identidades de dimensões que queremos. No nosso caso,
dimensão N.


Printamos a mensagem Matrix(NxN), como pedido no enunciado e printamos
a matriz em si. Por fim, incrementa-se o valor de W para passar
para o próximo cenário.

'''

from random import randint
import numpy as np

T = randint(1,5)
print (f'Teremos {T} cenários.')

W = 1

while W <= T:
    N = randint(0,20)
    print(f'N = {N}')
    t = np.eye(N)
    print(f'Matrix({N}x{N})')
    print(t)
    W += 1
