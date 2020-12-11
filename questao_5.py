'''
Breve análise:


Inicialmente escolhemos e printamos o número de cenários T de forma
aleatório em uma faixa de 0 a 5, também escolhida aleatóriamente.


Em seguida, definimos uma variável W para nos auxiliar na iteração dos
cenários, iteração esta feita pelo primeiro loop while.


Dentro deste primeiro loop while pedimos que o usuário insira uma
palavra S com as restrições colocadas pelo enunciado, isto é, o número
de letras dessa palavra deve ser maior que um e menor que cento e um.
Para isto, foi feito o segundo loop while.


Seguindo pelo código, printamos a palavra inserida com todas as letras
maiúsculas, seguindo o que foi feito no exemplo do enunciado da questão.


Depois, criamos uma variável abc que recebe a lista das letras do
alfabeto. Como na lista as letras são minúsculas, transformamos as
letras da palavra (string) S recebida em minúsculas para podermos
compará-las com as que estão em abc e atender a especificação do
enunciado que pede que S só contenha letras.


Também criamos a variável invalido para que, mais tarde no código
possamos utilizá-la caso algum caracter indesejado tenha sido inserido
e para que printemos a mensagem 'entrada inválida'.


O bloco do loop for que aparece em seguida compara cada caracter de S
inserido com os caracteres da lista abc. Caso esteja na lista, isto é,
caso sejam uma letra do alfabeto o código não faz nada, simplesmente
segue, caso contrário, a variável invalido passa de False para True.


Depois, colocamos a variável S com todas as letras maiúsculas novamente,
para que quando a substring seja extraída dela e printada esteja com
letras maiúsculas como no exemplo do enunciado. Definimos também as
variáveis a, d(auxiliam na inspeção das substrings palíndromas dentro da
string S), setando seus valores como zero e dois para que ele comece
pegando intervalos de duas em duas letras na palavra inserida e depois
vá aumentando. A variável l é o tamanho da string S, definimos uma
variável Q vazia para que depois ela receba a substrig palíndroma e
definimos também uma variável iteracao, igual a zero para que
possamos contar o número de iterações.


Após isso, criamos o loop while para que possamos incrementar o
intervalo de letras inspecionadas na string até que o intervalo seja
igual ao próprio tamanho da string, isto é, primeiro ele inspeciona
de duas em duas palavras, depois de três em três e assim até que ele
inspecione a palavra inteira. O loop while seguinte serve para passar
para o próximo intervalo de letras, isto é, primeiro ele inspeciona
as duas primeiras letras, depois as segunda e a terceira letras,
depois as terceira e quarta letras e assim por diante. Se o intervalo
de palavras inspecionado for um palíndromo, então a variável Q guarda
este palíndromo, isto é o loop if.


Finalmente, o loop if/elif/else serve para printar o palíndromo caso
seja válido, a mensagem de entrada inválida, caso algum caracter
indesejado faça oparte da string S inserida e a mensagem
'sem resultados', caso não haja substring  paléindroômica. Por fim,
incrementa-se o valor de W para passar para o próximo cenário.

'''

import string
from random import randint



T = randint(1,5)
print (f'Teremos {T} cenários.')

W = 1

while W <= T:
    S = str(input(f'Escreva uma palavra com pelo menos duas e até cem letras para o {W}º cenário:'))

    
    while len(S) < 2 or len(S) > 100:
        S = str(input(f'\nEsta palavra contém um número de letras inadequado.Por favor, escreva uma palavra com pelo menos duas e até cem letras para o {W}º cenário:\n'))
    
    print(f'\nPalavra inserida é {S.upper()}\n')

    
    abc = list(string.ascii_lowercase)
    S = S.lower()
    invalido = False
    
    for i in S:
        if i in abc:
            pass
        else:
            invalido = True
            break

    S = S.upper()
    a = 0
    d = 2
    l = len(S)
    Q = ''
    iteracao = 0
    
    while d <= l:
        while d <= l:
            if S[a:d] == S[a:d][::-1]:
                Q = S[a:d]
            a += 1
            d += 1
        iteracao += 1
        a = 0
        d = 2 + iteracao
        
    if Q != '' and invalido == False:
        print(f'A maior subsequência que é um palíndromo é {Q}.\n')
        
    elif invalido == True:
        print('entrada inválida\n')
        
    else:
        print('sem resultados\n')
        
    W += 1






         
