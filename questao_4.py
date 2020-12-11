'''
Breve análise:


Inicialmente escolhemos e printamos o número de cenários T de forma
aleatório em uma faixa de 0 a 5, também escolhida aleatóriamente.


Em seguida, definimos uma variável W para nos auxiliar na iteração dos
cenários, iteração esta feita pelo primeiro loop while.


Dentro deste primeiro loop while pedimos que o usuário insira uma
palavra S com as restrições colocadas pelo enunciado, isto é, o número
de letras dessa palavra deve ser maior que um e menor que cento e um.
Para garantir isto, foi feito o segundo loop while.


Seguindo pelo código, pedimos que o usuário insira um caractere C.
Printamos tanto a palavra S quanto o caractere C inseridos com todas
as letras maiúsculas, seguindo o que foi feito no exemplo do enunciado
da questão.


Depois, criamos uma variável abc que recebe a lista das letras do
alfabeto. Como na lista as letras são minúsculas, transformamos o
caractere C recebido em minúsculo para podermos compará-lo com as
letras que estão em abc e atender a especificação do
enunciado que pede que C pertença ao intervalo [a,z].


Também criamos a variável invalido para que, mais tarde no código
possamos utilizá-la caso algum caracter indesejado tenha sido inserido
em C e para que printemos a mensagem 'consulta inválida'.


O bloco do loop if que aparece em seguida compara o caractere C inserido
com os caracteres da lista abc e verifica se o seu tamanho é igual a um,
como pedido no enunciado. Caso essas demandas sejam atendidas, isto é,
caso sejam uma letra do alfabeto e tenha sido inserido apenas um caractere,
o código não faz nada, simplesmente segue, caso contrário, a variável
invalido passa de False para True.


Depois, colocamos as variáveis S e C com todas as letras maiúsculas novamente,
para que a saída fique no mesmo formato do exemplo do enunciado.


Definimos também a variável r, que recebe os valores de cada letra da palavra
e o números de suas ocorrências, como em um dicionário, onde há chave e valor.


Em seguida, fazemos um loop for para que os items de r sejam printados e depois
um loop if/else para garantir que as demandas em relação ao caractere C sejam atendidas.


Por fim, incrementa-se o valor de W para passar para o próximo cenário.

'''

from collections import Counter
from random import randint
import string

T = randint(1,5)
print (f'Teremos {T} cenários.')

W = 1

while W <= T:
    S = str(input(f'Escreva uma palavra com pelo menos duas e até cem letras \
para o {W}º cenário:'))
    
    while len(S) <= 1 or len(S) >= 100:
        S = str(input(f'Esta palavra contém um número de letras inadequado. \
Por favor, escreva uma palavra com pelo menos duas e até cem letras para o\
{W}º cenário:'))
        
    C = str(input(f'Insira um caractere:'))
    print(f'{S.upper()} {C.upper()}')
    
    abc = list(string.ascii_lowercase)
    C = C.lower()
    invalido = False
    
    if C in abc and len(C) == 1:
        pass
    
    else:
        invalido = True

    S = S.lower()
    C = C.lower()
    r = Counter(S)
    
    for letra in r.items():
        print(letra)

        
    if invalido == False:
        print(r[C])
        
    else:
        print('consulta inválida')
        
    W += 1

