'''
Breve análise:


Inicialmente escolhemos e printamos o número de cenários T de forma
aleatório em uma faixa de 0 a 5, também escolhida aleatóriamente.


Em seguida, definimos uma variável W para nos auxiliar na iteração dos
cenários, iteração esta feita pelo primeiro loop while.


Dentro deste primeiro loop while pedimos que o usuário insira um
número inteiro N com as restrições colocadas pelo enunciado, isto é,
um número inteiro maior ou igual a zero e menor ou igual a sessenta.
Para isto, foi feito o segundo loop while.


Seguindo pelo código, printamos o número inteiro inserido.


Criamos as variáveis a e b para que assumam os valores do penúltimo e
último números, respectivamente, da sequência de fibonacci, já que o
próximo número se dá pela soma dos dois anteriores. Como a sequência
começa com os números 0 e 1, colocamos estes valores em a e b. 


Depois, caso os números N inseridos sejam 0 ou 1, seus correspondentes
de Fibonacci também serão 0 e 1, respectivamente, caso contrário é
necessário calculá- lo. Portanto, é feita esta lógica de if/elif/else.


Para o cálculo de correspondentes de Fibonacci para N maior ou igual a
dois, criamos a variável indice e o loop while. A variável indice tem
valor inicial igual a dois e enquanto essa variável for menor que N, o
bloco calcula os números da sequência de Fibonacci e incrementa indice.
Quando o valor de indice é igual ao valor de N, o bloco terá calculado
o correspondente de Fibonacci para N a partir da soma dos dois
correspondentes de Fibonacci anteriores.

Em seguida, printamos o valor do correspondente de Fibonacci no formato
pedido no enunciado. Por fim, incrementa-se o valor de W para passar
para o próximo cenário.

'''

from random import randint

T = randint(1,5)
print (f'Teremos {T} cenários.')

W = 1

while W <= T:
    N = int(input(f'Insira um número inteiro N maior ou igual a zero e \
menor ou igual a sessenta \npara o {W}º cenário:'))
    
    while (N > 60) or (N < 0):
        N = int(input(f'\nEste número não é adequado. Por favor insira um\
número inteiro N maior ou igual \na zero e menor ou igual a sessenta para\
o {W}º cenário:'))

    print(f'\nO número inserido é {N}.')
    
    a = 0
    b = 1

    if N == 0:
        X = 0    
    elif N == 1:
        X = 1
    else:
        indice = 2
        while indice <= N:
            X = a + b
            a = b
            b = X
            indice += 1
        
    print(f'\nFib({N}) = {X}\n')
    W += 1







